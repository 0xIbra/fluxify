from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
from fluxify.utils import Utils
import parser
import gc


class XMLHandler:

    def __init__(self, filepath, mapping, item_node, root_node=None, error_tolerance=False):
        self.filepath = filepath
        self.mapping = mapping
        self.item_node = item_node
        self.root_node = root_node
        self.error_tolerance = error_tolerance

    def process(self):
        from xml.etree import ElementTree as ET

        self.xml = ET.parse(self.filepath)

        result = []
        for xmlitem in self.xml.findall(self.item_node):
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
                elif 'value' in yaml_value:
                    finalvalue = yaml_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

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

            result.append(item)

        return result

    def lazy_process(self):
        import lxml.etree as ET

        self.xml = ET.iterparse(self.filepath)

        result = []
        for ev, elem in iter(self.xml):

            if elem.tag == self.item_node:
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
                    elif 'value' in map_value:
                        finalvalue = map_value['value']
                        if type(finalvalue) == str:
                            finalvalue = finalvalue.replace('$subject', 'item')
                            expr = parser.expr(finalvalue)
                            finalvalue = eval(expr.compile(''))

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

        return subject

    def set_bulksize(self, size):
        self.bulksize = size

    def set_callback(self, callback):
        self.callback = callback

