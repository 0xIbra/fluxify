from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
import pandas as pd
import parser

class CSVHandler:

    def __init__(self, filepath, mapping, delimiter=',', skip_blank_lines=False, skip_header=False):
        self.filepath = filepath
        self.mapping = mapping
        self.delimiter = delimiter
        self.skip_header = skip_header

        self.csv = pd.read_csv(filepath, delimiter=delimiter, skip_blank_lines=skip_blank_lines, header=None)

    def process(self):
        result = []
        csv_generator = self.csv.T.iteritems()
        if self.skip_header:
            next(csv_generator)

        for data, row in csv_generator:
            item = {}
            for key, value in self.mapping.items():
                if 'col' in value:
                    col = int(value['col'])
                    finalvalue = row[col]
                    if 'transformations' in value:
                        finalvalue = handle_transformations(value['transformations'], finalvalue)
                    item = apply_value(item, key, finalvalue)

                    if 'conditions' in value:
                        finalvalue = handle_conditions(value['conditions'], item, row)
                        item = apply_value(item, key, finalvalue)
                elif 'value' in value:
                    finalvalue = value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    item = apply_value(item, key, finalvalue)

                    if 'conditions' in value:
                        finalvalue = handle_conditions(value['conditions'], item)
                        item = apply_value(item, key, finalvalue)
                elif 'conditions' in value:
                    finalvalue = handle_conditions(value['conditions'], item, row)
                    item = apply_value(item, key, finalvalue)

            result.append(item)
        
        return result