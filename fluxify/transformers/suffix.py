from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def suffix(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"suffix" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    suffix = transformation['args'][0]

    if value is not None and value != '':
        value = value + suffix

    return value
