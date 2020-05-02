from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def replace(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"search" (index: 0) argument was not found in transformation mapping.')

    if not list_index_exists(transformation['args'], 1):
        raise ArgumentNotFoundException('"replace" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    search = transformation['args'][0]
    new = transformation['args'][1]

    return str(value).replace(search, new)
