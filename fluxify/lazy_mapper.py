class LazyMapper:
    CSV_FORMAT = 'csv'
    JSON_FORMAT = 'json'
    XML_FORMAT = 'xml'
    FORMATS = [CSV_FORMAT, JSON_FORMAT, XML_FORMAT]

    def __init__(self, _type='csv', error_tolerance=False, bulksize=100):
        self.__type = _type
        self.__error_tolerance = error_tolerance
        self.__bulksize = bulksize
        self.__callback = None

    def map(self, filepath, mapping, delimiter=',', skip_blank_lines=False, root_node=None, item_node=None, skip_header=False):
        if self.__type == 'csv':
            pass
        elif self.__type == 'json':
            from fluxify.handler.json import JSONHandler

            handler = JSONHandler(filepath, mapping, root_node, self.__error_tolerance, self.__bulksize)
            if not self.__check_callback():
                raise Exception('[error] Callback must be defined')

            handler.set_callback(self.__callback)
            handler.lazy_process()
        elif self.__type == 'xml':
            pass
        else:
            raise Exception('[error] Unsupported format "{}"'.format(self.__type))

    def set_bulksize(self, size):
        self.__bulksize = size

    def set_callback(self, callback):
        self.__callback = callback

    def __check_callback(self):
        return self.__callback is not None