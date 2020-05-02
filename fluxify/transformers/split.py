from fluxify.exceptions import ArgumentNotFoundException, InvalidArgumentException
from fluxify.transformers import list_index_exists, validate_transformation_args


def split(transformation):
    validate_transformation_args(transformation)

    if len(transformation['args']) == 0:
        raise Exception('"args" cannot be empty, delimiter must be specified as the first index.')

    value = transformation['value']
    delimiter = transformation['args'][0]

    if list_index_exists(transformation['args'], 1):
        index = transformation['args'][1]
        split = value.split(delimiter)

        return split[index]

    result = value.split(delimiter)
    if type(result) is list:
        if len(result) == 1 and result[0] == '':
            result = []

    return result
