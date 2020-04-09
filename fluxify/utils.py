from datetime import datetime
import math


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

    @staticmethod
    def clean_if_nan(value):
        if type(value) is int or type(value) is float:
            if math.isnan(value):
                value = None

        return value

    @staticmethod
    def check_for_nan(value):
        if type(value) is int or type(value) is float:
            if math.isnan(value):
                return True

        return False

    @staticmethod
    def empty(value):
        if value == '' or value == ' ':
            return True

        if value is None:
            return True

        if value == {}:
            return True

        if type(value) is list:
            return len(value) <= 0

        return False
