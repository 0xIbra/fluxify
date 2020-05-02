from fluxify.transformers import validate_transformation_args, list_index_exists
from fluxify.exceptions import ArgumentNotFoundException
import re


def capture(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"pattern" (index: 0) argument was not found in transformation mapping.')

    if not list_index_exists(transformation['args'], 1):
        raise ArgumentNotFoundException('"group_number" (index: 1) argument was not found in transformation mapping.')

    value = transformation['value']
    pattern = transformation['args'][0]
    group_number = transformation['args'][1]
    flag = None

    if list_index_exists(transformation['args'], 2):
        arg3 = transformation['args'][2]
        if arg3 == 'i':
            flag = re.IGNORECASE
        elif arg3 == 'm':
            flag = re.MULTILINE

    if pattern[:1] == '/':
        if pattern[-2:] == '/i':
            flag = re.IGNORECASE
            pattern = remove_at(0, pattern)
            pattern = remove_at(len(pattern) - 1, pattern)
            pattern = remove_at(len(pattern) - 1, pattern)
        elif pattern[-2:] == '/m':
            flag = re.MULTILINE
            pattern = remove_at(0, pattern)
            pattern = remove_at(len(pattern) - 1, pattern)
            pattern = remove_at(len(pattern) - 1, pattern)

    if flag is None:
        result = re.match(pattern, value).group(group_number)
    else:
        result = re.match(pattern, value, flags=flag).group(group_number)

    return result


def remove_at(i, s):
    return s[:i] + s[i+1:]
