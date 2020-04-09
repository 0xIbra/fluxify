from fluxify.exceptions import ArgumentNotFoundException


def replace(transformation):
    if not 'value' in transformation:
        raise ArgumentNotFoundException('"value" argument was not found in transformation mapping.')

    if not 'search' in transformation:
        raise ArgumentNotFoundException('"search" argument was not found in transformation mapping.')

    if not 'new' in transformation:
        raise ArgumentNotFoundException('"new" argument was not found in transformation mapping.')

    value = transformation['value']
    search = transformation['search']
    new = transformation['new']

    return str(value).replace(search, new)
