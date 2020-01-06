from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
from xml.etree import ElementTree as ET
import parser

class XMLHandler:

    def __init__(self, filepath, mapping, item_node, root_node=None):
        self.filepath = filepath
        self.mapping = mapping
        self.item_node = item_node
        self.root_node = root_node

        self.xml = ET.parse(filepath)

    def process(self):
        result = []
        for xmlitem in self.xml.findall(self.item_node):
            item = {}
            for yaml_key, yaml_value in self.mapping.items():
                if 'col' in yaml_value:
                    col = yaml_value['col']
                    finalvalue = self.get(col, xmlitem)
                    if 'transformations' in yaml_value:
                        finalvalue = handle_transformations(yaml_value['transformations'], finalvalue)
                    item = apply_value(item, yaml_key, finalvalue)
                elif 'value' in yaml_value:
                    finalvalue = yaml_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    item = apply_value(item, yaml_key, finalvalue)
                elif 'conditions' in yaml_value:
                    finalvalue = handle_conditions(yaml_value['conditions'], item)
                    item = apply_value(item, yaml_key, finalvalue)

            result.append(item)

        return result


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