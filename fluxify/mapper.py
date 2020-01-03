from fluxify.transformers.transformer import TRANSFORMERS

class Mapper:

    def map(self, filepath, mapping, Type='csv'):
        self.type = Type

        if self.type == 'csv':
            from fluxify.handler.csv import CSVHandler
            
            handler = CSVHandler(filepath, mapping)
            return handler.process()
        elif self.type == 'json':
            from fluxify.handler.json import JSONHandler

            handler = JSONHandler(filepath, mapping)
            return handler.process()
        elif self.type == 'xml':
            pass
        elif self.type == 'txt':
            pass