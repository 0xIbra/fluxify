from fluxify.transformers.transformer import TRANSFORMERS

class Mapper:

    def map(self, filepath, mapping, Type='csv', delimiter=',', skip_blank_lines=False, root_node=None, item_node=None):
        self.type = Type

        if self.type == 'csv':
            from fluxify.handler.csv import CSVHandler

            handler = CSVHandler(filepath, mapping, delimiter=delimiter, skip_blank_lines=skip_blank_lines)
            return handler.process()
        elif self.type == 'json':
            from fluxify.handler.json import JSONHandler

            handler = JSONHandler(filepath, mapping, root_node=root_node)
            return handler.process()
        elif self.type == 'xml':
            from fluxify.handler.xmlh import XMLHandler

            handler = XMLHandler(filepath, mapping, item_node=item_node, root_node=root_node)
            return handler.process()
        else:
            print('[error] Unsupported format "{}"'.format(self.type))
            exit(1)