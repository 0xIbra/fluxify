class Mapper:
    CSV_FORMAT = 'csv'
    JSON_FORMAT = 'json'
    XML_FORMAT = 'xml'
    FORMATS = [CSV_FORMAT, JSON_FORMAT, XML_FORMAT]

    def __init__(self, _type='csv', error_tolerance=False):
        self.type = _type
        self.error_tolerance = error_tolerance

        self.__stats = None

    def map(self, filepath, mapping, delimiter=',', skip_blank_lines=False, root_node=None, item_node=None, skip_header=False):
        if self.type == 'csv':
            from fluxify.handler.csv import CSVHandler

            handler = CSVHandler(filepath, mapping, delimiter=delimiter, skip_blank_lines=skip_blank_lines, skip_header=skip_header, error_tolerance=self.error_tolerance)

            result = handler.process()

            self.__stats = handler.get_stats()

            return result
        elif self.type == 'json':
            from fluxify.handler.json import JSONHandler

            handler = JSONHandler(filepath, mapping, root_node=root_node, error_tolerance=self.error_tolerance)

            result = handler.process()

            self.__stats = handler.get_stats()

            return result
        elif self.type == 'xml':
            from fluxify.handler.xmlh import XMLHandler

            handler = XMLHandler(filepath, mapping, item_node=item_node, root_node=root_node, error_tolerance=self.error_tolerance)

            result = handler.process()

            self.__stats = handler.get_stats()

            return result
        else:
            raise Exception('[error] Unsupported format "{}"'.format(self.type))

    def get_stats(self):
        return self.__stats
