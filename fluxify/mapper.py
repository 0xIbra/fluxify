from fluxify.transformers.transformer import TRANSFORMERS

class Mapper:

    def __init__(self, error_tolerance=False):
        self.error_tolerance = error_tolerance

    def map(self, filepath, mapping, Type='csv', delimiter=',', skip_blank_lines=False, root_node=None, item_node=None, skip_header=False):
        self.type = Type

        if self.type == 'csv':
            from fluxify.handler.csv import CSVHandler

            handler = CSVHandler(filepath, mapping, delimiter=delimiter, skip_blank_lines=skip_blank_lines, skip_header=skip_header, error_tolerance=self.error_tolerance)
            return handler.process()
        elif self.type == 'json':
            from fluxify.handler.json import JSONHandler

            handler = JSONHandler(filepath, mapping, root_node=root_node, error_tolerance=self.error_tolerance)
            return handler.process()
        elif self.type == 'xml':
            from fluxify.handler.xmlh import XMLHandler

            handler = XMLHandler(filepath, mapping, item_node=item_node, root_node=root_node, error_tolerance=self.error_tolerance)
            return handler.process()
        else:
            print('[error] Unsupported format "{}"'.format(self.type))
            exit(1)