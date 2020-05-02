from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def right(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"length" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    length = transformation['args'][0]

    return value[- length:]
