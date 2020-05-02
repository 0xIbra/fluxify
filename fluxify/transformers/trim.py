from fluxify.transformers import validate_transformation_args
from fluxify.exceptions import InvalidArgumentException


def trim(transformation):
    validate_transformation_args(transformation)

    value = transformation['value']
    if type(value) is not str:
        raise InvalidArgumentException('"value" for "trim" transformer must be a string. {} given.'.format(type(value)))

    value = value.replace(' ', '')

    return value
