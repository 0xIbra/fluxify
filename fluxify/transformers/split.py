from fluxify.exceptions import ArgumentNotFoundException


def split(transformation):
    if 'delimiter' not in transformation:
        raise ArgumentNotFoundException('"delimiter" was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['delimiter']

    if 'index' in transformation:
        index = transformation['index']
        split = value.split(delimiter)

        return split[index]

    result = value.split(delimiter)
    if type(result) is list:
        if len(result) == 1 and result[0] == '':
            result = []

    return result
