from helper.yamlparser import apply_value
import pandas as pd

class CSVHandler:

    def __init__(self, filepath, mapping, delimiter=',', header='infer'):
        self.filepath = filepath
        self.mapping = mapping
        self.delimiter = delimiter
        
        self.csv = pd.read_csv(filepath, skip_blank_lines=True, delimiter=delimiter, header=header)

    def process(self):
        result = []
        for data, row in self.csv.T.iteritems():
            item = {}
            for key, value in self.mapping.items():
                if 'col' in value:
                    col = int(value['col'])
                    item = apply_value(item, key, row[col])
                elif 'value' in value:
                    item = apply_value(item, key, value['value'])
                
                # if 'transformations' in value:
                    

            result.append(item)
        
        return result