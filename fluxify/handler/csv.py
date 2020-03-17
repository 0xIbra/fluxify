from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
from fluxify.utils import Utils
import pandas as pd
import parser


class CSVHandler:

    def __init__(self, filepath, mapping, delimiter=',', skip_blank_lines=False, skip_header=False, error_tolerance=False, bulksize=100):
        self.filepath = filepath
        self.mapping = mapping
        self.delimiter = delimiter
        self.skip_blank_lines = skip_blank_lines
        self.skip_header = skip_header
        self.bulksize = bulksize

        self.error_tolerance = error_tolerance

    def process(self):
        self.csv = pd.read_csv(self.filepath, delimiter=self.delimiter, skip_blank_lines=self.skip_blank_lines, header=None)
        self.csv = self.csv.values

        result = []

        for it, data in enumerate(self.csv):
            # Skipping the first line if needed
            if self.skip_header and it == 0:
                continue

            item = {}
            for map_key, map_value in self.mapping.items():

                if 'col' in map_value:
                    col = int(map_value['col'])
                    finalvalue = data[col]

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=self.error_tolerance)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'value' in map_value:
                    finalvalue = map_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'conditions' in map_value:
                    finalvalue = handle_conditions(map_value['conditions'], item, data)
                    item = apply_value(item, map_key, finalvalue)
                else:
                    text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(map_key)
                    if self.error_tolerance:
                        Utils.log('error', text)
                        continue
                    else:
                        raise Exception(text)

            result.append(item)

        return result

    def lazy_process(self):
        self.csv = pd.read_csv(self.filepath, delimiter=self.delimiter, skip_blank_lines=self.skip_blank_lines, header=None)
        csv_generator = self.csv.T.iteritems()

        result = []

        if self.skip_header:
            next(csv_generator)

        for it, data in csv_generator:
            item = {}
            # Iterating through the mapping
            for map_key, map_value in self.mapping.items():
                if 'col' in map_value:
                    col = int(map_value['col'])
                    finalvalue = data[col]

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=False)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'value' in map_value:
                    finalvalue = map_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=True)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'conditions' in map_value:
                    finalvalue = handle_conditions(map_value['conditions'], item, data)
                    item = apply_value(item, map_key, finalvalue)
                else:
                    text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(map_key)
                    if self.error_tolerance:
                        Utils.log('error', text)
                        continue
                    else:
                        raise Exception(text)

            result.append(item)
            if (self.bulksize % len(result)) == 0:
                self.callback(result)
                result = []

        if len(result) > 0:
            self.callback(result)
            result = []

    def set_bulksize(self, size):
        self.bulksize = size

    def set_callback(self, callback):
        self.callback = callback
