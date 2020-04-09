from fluxify.exceptions import ArgumentNotFoundException


def split(transformation):
    if not 'delimiter' in transformation:
        raise ArgumentNotFoundException('"delimiter" was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['delimiter']

    if 'index' in transformation:
        index = transformation['index']
        split = value.split(delimiter)

        return split[index]

    return value.split(delimiter)