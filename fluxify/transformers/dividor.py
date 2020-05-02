from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def dividor(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('[fluxify][dividor] Value not found to divide with.')

    value = transformation['value']
    divide_value = transformation['args'][0]

    return value / divide_value
