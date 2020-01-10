def replace(transformation):
    if not 'value' in transformation:
        raise Exception('"value" argument was not found in transformation mapping.')

    if not 'search' in transformation:
        raise Exception('"search" argument was not found in transformation mapping.')

    if not 'new' in transformation:
        raise Exception('"new" argument was not found in transformation mapping.')

    value = transformation['value']
    search = transformation['search']
    new = transformation['new']

    return str(value).replace(search, new)