from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def array_walk(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"dimension/path" (index: 0) argument was not found in transformation mapping.')

    if not list_index_exists(transformation['args'], 1):
        raise ArgumentNotFoundException('"index" (index: 1) argument was not found in transformation mapping.')

    value = transformation['value']

    dimensions = str(transformation['args'][0]).split('.')
    key = transformation['args'][1]

    if dimensions[0] == '':
        return []

    if type(value) is dict and len(value) > 0:
        pass
    elif type(value) is list and len(value) > 0:
        pass
    else:
        return []
