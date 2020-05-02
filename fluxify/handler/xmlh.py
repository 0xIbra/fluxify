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
        self.__error_tolerance = error_tolerance
        self.__save_unmatched = save_unmatched
        self.__unmatched_key = unmatched_key

        self.xml = None

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

                    multiple = None
                    value_index = None
                    default = None
                    raw = True

                    if 'multiple' in yaml_value:
                        multiple = yaml_value['multiple']

                    if 'index' in yaml_value:
                        value_index = yaml_value['index']

                    if 'default' in yaml_value:
                        default = yaml_value['default']

                    if 'raw' in yaml_value:
                        raw_ = yaml_value['raw']
                        if type(raw_) is bool:
                            raw = raw_

                    if col == '_all_':
                        finalvalue = xmlitem
                    elif col.startswith('@attributes.'):
                        try:
                            finalvalue = xmlitem.attrib[col.replace('@attributes.', '')]
                        except:
                            # TODO: Maybe log something ?
                            finalvalue = None
                    else:
                        finalvalue = self.get(col, xmlitem, multiple, value_index, default, raw)

                    transformations = []

                    if 'transformation' in yaml_value:
                        transformations.append(yaml_value['transformation'])

                    if 'transformations' in yaml_value:
                        map_transformations = yaml_value['transformations']
                        if type(map_transformations) is list:
                            for tr in map_transformations:
                                transformations.append(tr)

                    # If transformations are defined in the mapping, applying them
                    if len(transformations) > 0:
                        finalvalue = handle_transformations(transformations, finalvalue,
                                                            error_tolerance=self.__error_tolerance)

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
                    if self.__error_tolerance:
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

                        multiple = None
                        value_index = None
                        default = None
                        raw = True

                        if 'multiple' in map_value:
                            multiple = map_value['multiple']

                        if 'index' in map_value:
                            value_index = map_value['index']

                        if 'default' in map_value:
                            default = map_value['default']

                        if 'raw' in map_value:
                            raw_ = map_value['raw']
                            if type(raw_) is bool:
                                raw = raw_

                        if col == '_all_':
                            finalvalue = elem
                        elif col.startswith('@attributes.'):
                            try:
                                finalvalue = elem.attrib[col.replace('@attributes.', '')]
                            except:
                                finalvalue = None
                        else:
                            finalvalue = self.get(col, elem, multiple, value_index, default, raw)

                        transformations = []

                        if 'transformation' in map_value:
                            transformations.append(map_value['transformation'])

                        if 'transformations' in map_value:
                            map_transformations = map_value['transformations']
                            if type(map_transformations) is list:
                                for tr in map_transformations:
                                    transformations.append(tr)

                        # If transformations are defined in the mapping, applying them
                        if len(transformations) > 0:
                            finalvalue = handle_transformations(transformations, finalvalue,
                                                                error_tolerance=self.__error_tolerance)

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
                        if self.__error_tolerance:
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

    def get(self, key, subject, multiple=None, value_index=None, default=None, raw=True):
        split = key.split('.')
        split_count = len(split)
        for index, val in enumerate(split):
            if '$subject' == val:
                continue

            it = index + 1

            if it != split_count:
                value = subject.find(val)
            else:
                value = subject.findall(val)

            if value is None:
                if default is None:
                    return False
                else:
                    return default

            if type(value) is list and len(value) == 0:
                if default is None:
                    return False
                else:
                    return default

            if it == split_count:
                if type(value) is not list:
                    if not multiple:
                        if raw:
                            subject = value.text
                        else:
                            subject = value
                    else:
                        res = []
                        if raw:
                            res.append(value.text)
                        else:
                            res.append(value)
                        subject = res
                else:
                    if multiple is False:
                        if not value_index:
                            if raw:
                                subject = value[0].text
                            else:
                                subject = value[0]
                        else:
                            if type(value_index) is int:
                                try:
                                    if raw:
                                        subject = value[value_index].text
                                    else:
                                        subject = value[value_index]
                                except:
                                    if default is None:
                                        subject = False
                                    else:
                                        subject = default
                    elif multiple is None:
                        res = None
                        if len(value) > 1:
                            res = []
                            if not value_index:
                                for item in value:
                                    if raw:
                                        res.append(item.text)
                                    else:
                                        res.append(item)
                            else:
                                if type(value_index) is int:
                                    try:
                                        if raw:
                                            res = value[value_index].text
                                        else:
                                            res = value[value_index]
                                    except:
                                        if default is None:
                                            res = False
                                        else:
                                            res = default
                        else:
                            if raw:
                                res = value[0].text
                            else:
                                res = value[0]

                        subject = res
                    else:
                        res = []
                        if not value_index:
                            for item in value:
                                if raw:
                                    res.append(item.text)
                                else:
                                    res.append(item)

                            subject = res
                        else:
                            if type(value_index) is int:
                                try:
                                    if raw:
                                        res.append(value[value_index].text)
                                    else:
                                        res.append(value[value_index])
                                except:
                                    pass

                                subject = res
            else:
                subject = value

        # Set to None if value is NaN
        subject = Utils.clean_if_nan(subject)

        if subject is None and default is not None:
            subject = default

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
                remove_val = subject.find(val)
                if remove_val is not None:
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
