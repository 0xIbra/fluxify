from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def prefix(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"prefix" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    prefix = transformation['args'][0]

    if value is not None and value != '':
        value = prefix + value

    return value
