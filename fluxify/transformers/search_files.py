from fluxify.transformers import validate_transformation_args, list_index_exists
from fluxify.exceptions import ArgumentNotFoundException
from glob import glob


def search_files(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"pattern" (index: 0) was not found in transformation mapping.')

    pattern = transformation['args'][0]
    recursive = False
    if list_index_exists(transformation['args'], 1):
        arg2 = transformation['args'][1]
        if type(arg2) is bool:
            recursive = arg2

    value = glob(pattern, recursive=recursive)

    return value
