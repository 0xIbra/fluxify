from fluxify.handler.conditions import handle_conditions
from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.utils import Utils
import parser
import gc


class JSONHandler:

    def __init__(self, filepath, mapping, root_node=None, error_tolerance=False, bulksize=100):
        self.__filepath = filepath
        self.__mapping = mapping
        self.__root_node = root_node
        self.__error_tolerance = error_tolerance
        self.__bulksize = bulksize

    def process(self):
        import json

        with open(self.__filepath, 'r') as fh:
            jsoncontent = fh.read()
            self.json = json.loads(jsoncontent)

        result = []
        content = self.json
        for jsonitem in content:
            item = {}
            for yaml_key, yaml_value in self.__mapping.items():
                if 'col' in yaml_value:
                    col = yaml_value['col']
                    finalvalue = self.get(col, jsonitem)
                    if 'transformations' in yaml_value:
                        finalvalue = handle_transformations(yaml_value['transformations'], finalvalue, error_tolerance=self.__error_tolerance)

                    item = apply_value(item, yaml_key, finalvalue)

                    if 'conditions' in yaml_value:
                        finalvalue = handle_conditions(yaml_value['conditions'], item, jsonitem)
                        item = apply_value(item, yaml_key, finalvalue)
                elif 'value' in yaml_value:
                    finalvalue = yaml_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    # Clean if NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    item = apply_value(item, yaml_key, finalvalue)

                    if 'conditions' in yaml_value:
                        finalvalue = handle_conditions(yaml_value['conditions'], item)
                        item = apply_value(item, yaml_key, finalvalue)
                elif 'conditions' in yaml_value:
                    finalvalue = handle_conditions(yaml_value['conditions'], item)

                    # Set to None if value is NaN
                    Utils.clean_if_nan(finalvalue)

                    item = apply_value(item, yaml_key, finalvalue)

            result.append(item)

        return result

    def lazy_process(self):
        import ijson

        root_node = 'item'
        if self.__root_node is not None and self.__root_node is str:
            root_node = '{}.item'.format(self.__root_node)

        with open(self.__filepath, 'rb') as fh:
            self.__content = ijson.items(fh, root_node)
            results = []
            it = 0

            # Iterating over JSON generator
            for jsonobject in self.__content:
                item = {}

                # For each JSON Object, iterating over the YAML mapping and retrieving data
                for yaml_key, yaml_value in self.__mapping.items():

                    if 'col' in yaml_value:
                        col = yaml_value['col']
                        finalvalue = self.get(col, jsonobject)

                        # If transformations are defined in the mapping, applying them
                        if 'transformations' in yaml_value:
                            finalvalue = handle_transformations(yaml_value['transformations'], finalvalue, error_tolerance=self.__error_tolerance)

                        item = apply_value(item, yaml_key, finalvalue)

                        # Handling conditions
                        if 'conditions' in yaml_value:
                            finalvalue = handle_conditions(yaml_value['conditions'], item, jsonobject)
                            item = apply_value(item, yaml_key, finalvalue)
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

                results.append(item)

                if len(results) % self.__bulksize == 0:
                    self.__callback(results)
                    results = []
                    gc.collect()

            if len(results) > 0:
                self.__callback(results)
                results = []
                gc.collect()

    def get(self, key, subject):
        split = key.split('.')
        for val in split:
            if not val in subject:
                return False
            subject = subject[val]


        # Set to None if value is NaN
        subject = Utils.clean_if_nan(subject)

        return subject

    def set_bulksize(self, size):
        self.__bulksize = size

    def set_callback(self, callback):
        self.__callback = callback
