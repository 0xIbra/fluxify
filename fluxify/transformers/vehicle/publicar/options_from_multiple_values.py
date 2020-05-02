from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def publicar_options_from_multiple_values(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"cols" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    cols = transformation['args'][0]
    delimiter = ','
    result = []

    if delimiter not in cols:
        return None

    cols_list = cols.split(delimiter)
    for col in cols_list:
        name = value[int(col)]
        try:
            result.append({
                'name': name,
                'original': name,
                'code': None,
                'description': None,
                'price': None
            })
        except:
            pass

    return result
