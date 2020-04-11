from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
from fluxify.utils import Utils
import parser
import gc


class XMLHandler:

    def __init__(self, filepath, mapping, item_node, root_node=None, error_tolerance=False,
                 save_unmatched=True, unmatched_key='unmatched'):
        self.filepath = filepath
        self.mapping = mapping
        self.item_node = item_node
        self.root_node = root_node
        self.error_tolerance = error_tolerance
        self.__save_unmatched = save_unmatched
        self.__unmatched_key = unmatched_key

        self.__stats = {
            'total_count': 0
        }

    def process(self):
        from xml.etree import ElementTree as ET

        self.xml = ET.parse(self.filepath)

        result = []
        for xmlitem in self.xml.findall(self.item_node):
            # Updating stats
            self.__stats['total_count'] += 1

            item = {}
            for yaml_key, yaml_value in self.mapping.items():
                if 'col' in yaml_value:
                    col = yaml_value['col']
                    finalvalue = self.get(col, xmlitem)
                    if 'transformations' in yaml_value:
                        finalvalue = handle_transformations(yaml_value['transformations'], finalvalue, error_tolerance=self.error_tolerance)
                    item = apply_value(item, yaml_key, finalvalue)

                    if 'conditions' in yaml_value:
                        finalvalue = handle_conditions(yaml_value['conditions'], item)
                        item = apply_value(item, yaml_key, finalvalue)

                    # Deleting the value from original input object
                    if self.__save_unmatched:
                        self.__delete(col, xmlitem)
                elif 'value' in yaml_value:
                    finalvalue = yaml_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    # Set to None if value is NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    item = apply_value(item, yaml_key, finalvalue)

                    if 'conditions' in yaml_value:
                        finalvalue = handle_conditions(yaml_value['conditions'], item)
                        item = apply_value(item, yaml_key, finalvalue)
                elif 'conditions' in yaml_value:
                    finalvalue = handle_conditions(yaml_value['conditions'], item)
                    item = apply_value(item, yaml_key, finalvalue)
                else:
                    text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(yaml_key)
                    if self.error_tolerance:
                        Utils.log('error', text)
                        continue
                    else:
                        raise Exception(text)

            # Unmatched
            if self.__save_unmatched:
                item[self.__unmatched_key] = self.__get_unmatched(xmlitem)

            result.append(item)

        return result

    def lazy_process(self):
        import lxml.etree as ET

        self.xml = ET.iterparse(self.filepath)

        result = []
        for ev, elem in iter(self.xml):

            if elem.tag == self.item_node:
                # Updating stats
                self.__stats['total_count'] += 1

                item = {}
                for map_key, map_value in self.mapping.items():
                    if 'col' in map_value:
                        col = map_value['col']
                        finalvalue = self.get(col, elem)
                        if 'transformations' in map_value:
                            finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=self.error_tolerance)

                        item = apply_value(item, map_key, finalvalue)

                        if 'conditions' in map_value:
                            finalvalue = handle_conditions(map_value['conditions'], item)
                            item = apply_value(item, map_key, finalvalue)

                        # Deleting the value from original input object
                        if self.__save_unmatched:
                            self.__delete(col, elem)
                    elif 'value' in map_value:
                        finalvalue = map_value['value']
                        if type(finalvalue) == str:
                            finalvalue = finalvalue.replace('$subject', 'item')
                            expr = parser.expr(finalvalue)
                            finalvalue = eval(expr.compile(''))

                        # Set to None if value is NaN
                        finalvalue = Utils.clean_if_nan(finalvalue)

                        item = apply_value(item, map_key, finalvalue)

                        if 'conditions' in map_value:
                            finalvalue = handle_conditions(map_value['conditions'], item)
                            item = apply_value(item, map_key, finalvalue)
                    elif 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item)
                        item = apply_value(item, map_key, finalvalue)
                    else:
                        text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(map_key)
                        if self.error_tolerance:
                            Utils.log('error', text)
                            continue
                        else:
                            raise Exception(text)

                # Unmatched
                if self.__save_unmatched:
                    item[self.__unmatched_key] = self.__get_unmatched(elem)

                result.append(item)
                if (len(result) % self.bulksize) == 0:
                    self.callback(result)
                    result.clear()
                    gc.collect()

                # Clearing the element now that the values have been extracted
                elem.clear()
                for ancestor in elem.xpath('ancestor-or-self::*'):
                    while ancestor.getprevious() is not None:
                        del ancestor.getparent()[0]

        if len(result) > 0:
            self.callback(result)
            result.clear()
            gc.collect()

    def get(self, key, subject):

        split = key.split('.')
        for index, val in enumerate(split):
            if '$subject' == val:
                continue

            value = subject.find(val)
            if value is None:
                return False

            it = index + 1
            if it == len(split):
                subject = value.text
            else:
                subject = value

        # Set to None if value is NaN
        subject = Utils.clean_if_nan(subject)

        return subject

    def __get_unmatched(self, xmlitem, inputunmatched=None):
        unmatched = {}
        if inputunmatched is not None:
            unmatched = inputunmatched

        for ix, item in enumerate(list(xmlitem)):
            if self.__has_children(item):
                unmatched[item.tag] = {}
                self.__get_unmatched(item, unmatched[item.tag])
            else:
                value = Utils.clean_if_nan(item.text)
                if value is not None and not Utils.empty(value):
                    unmatched[item.tag] = value

        return unmatched

    def __delete(self, key: str, subject):
        split = key.split('.')
        for ix, val in enumerate(split):
            if '$subject' == val:
                continue

            if ix != len(split) - 1:
                subject = subject.find(val)
                if subject is None:
                    return False
            else:
                subject.remove(subject.find(val))

        return True

    def __has_children(self, element):
        return True if len(list(element)) else False

    def set_bulksize(self, size):
        self.bulksize = size

    def set_callback(self, callback):
        self.callback = callback

    def get_stats(self):
        return self.__stats
