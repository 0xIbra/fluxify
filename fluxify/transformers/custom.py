from fluxify.exceptions import ArgumentNotFoundException

def equipments_from_string(transformation):
    if not 'delimiter' in transformation:
        raise ArgumentNotFoundException('"delimiter" argument was not found in transformation mapping.')

    result = []
    delimiter = transformation['delimiter']

    value = transformation['value']
    for item in value.split(delimiter):
        if item.strip() == '':
            continue

        result.append({
            'name': item,
            'original': item,
            'value': None,
            'group': None
        })

    return result

def options_from_string(transformation):
    if not 'delimiter' in transformation:
        raise ArgumentNotFoundException('"delimiter" argument was not found in transformation mapping.')

    result = []
    delimiter = transformation['delimiter']

    value = transformation['value']
    for item in value.split(delimiter):
        if item.strip() == '':
            continue

        result.append({
            'name': item,
            'original': item,
            'code': None,
            'description': None,
            'price': None
        })

    return result