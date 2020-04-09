from datetime import datetime
from fluxify.exceptions import ArgumentNotFoundException


def date(transformation):
    if not 'in_format' in transformation:
        raise ArgumentNotFoundException('"in_format" was not found in transformation mapping.')

    if not 'out_format' in transformation:
        raise ArgumentNotFoundException('"out_format" was not found in transformation mapping.')

    value = transformation['value']
    in_format = transformation['in_format']
    out_format = transformation['out_format']

    dateobj = datetime.strptime(value, in_format)

    return dateobj.strftime(out_format)
