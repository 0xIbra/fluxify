from helper.yamlparser import apply_value
import pandas as pd

class CSVHandler:

    def __init__(self, filepath, mapping):
        self.filepath = filepath
        self.mapping = mapping
        
        self.csv = pd.read_csv(filepath, skip_blank_lines=True)

    def process(self):
        result = []
        for data, row in self.csv.T.iteritems():
            item = {}
            for key, value in self.mapping.items():
                col = int(value['col'])
                item = apply_value(item, key, row[col])
            
            result.append(item)
        
        return result