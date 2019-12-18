def split(transformation):
    if not 'delimiter' in transformation:
        raise Exception('"delimiter" was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['delimiter']

    return value.split(delimiter)