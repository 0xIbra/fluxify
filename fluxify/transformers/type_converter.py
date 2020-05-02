from fluxify.exceptions import ArgumentNotFoundException, InvalidArgumentException
from fluxify.transformers import list_index_exists, validate_transformation_args


def type_converter(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"type" (index: 0) argument was not found in transformation mapping.')

    type_str = transformation['args'][0]
    if type(type_str) is not str:
        raise InvalidArgumentException('"type" (index: 0) argument must be a string. {} given'.format(type(type_str)))

    nullable = False
    if list_index_exists(transformation['args'], 1):
        nullable = True

    value = transformation['value']

    if type_str == 'boolean':
        value = bool(value)
    elif type_str == 'array':
        if type(value) is not list:
            if value is not None:
                value = [value]
    elif type_str == 'int':
        if value is not None:
            value = int(value)
    elif type_str == 'string':
        if type(value) is list:
            if len(value) > 0:
                value = str(value[0])

        if value is not None:
            value = str(value)

    if nullable:
        if value == '' or value == 0 or value == 0.0 or value == {} or value == [] or value is False:
            value = None

    return value
