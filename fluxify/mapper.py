from transformers.split import split

class Mapper:
    def __init__(self, Type='csv'):
        self.type = Type
    
    def map(self, filepath, mapping):
        if self.type == 'csv':
            from handler.csv import CSVHandler
            
            handler = CSVHandler(filepath, mapping)
            return handler.process()
        elif self.type == 'json':
            pass
        elif self.type == 'xml':
            pass
        elif self.type == 'txt':
            pass