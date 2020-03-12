from datetime import datetime


class Utils:

    @staticmethod
    def getdatetime(format=None):
        datet = datetime.now()

        if format is None:
            return datet

        return datet.strftime(format)

    @staticmethod
    def log(level, message):
        _format = '%H:%M:%S %d-%m-%Y'
        text = '{} - [{}] : {}'.format(Utils.getdatetime(format=_format), level, message)
        print(text)
