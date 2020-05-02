from datetime import datetime
from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def date(transformation):
    if 'args' not in transformation:
        validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('Input format was not found in transformation arguments.')

    if not list_index_exists(transformation['args'], 1):
        raise ArgumentNotFoundException('Input format was not found in transformation arguments.')

    value = transformation['value']
    in_format = transformation['args'][0]
    out_format = transformation['args'][1]

    dateobj = datetime.strptime(value, in_format)

    return dateobj.strftime(out_format)
