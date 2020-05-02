from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def multiplicator(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('[fluxify][multiplicator] Value not found to multiply with.')

    value = transformation['value']
    multiply_value = transformation['args'][0]

    return value * multiply_value
