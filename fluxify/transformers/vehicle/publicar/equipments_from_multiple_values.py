from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def publicar_equipments_from_multiple_values(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"cols" (index: 0) argument was not found in transformation mapping.')

    delimiter = ','
    cols_str = transformation['args'][0]

    value = transformation['value']
    result = []

    if delimiter not in cols_str:
        return None

    cols_list = str(cols_str).split(delimiter)
    for col in cols_list:
        equip = value[int(col)]
        result.append({
            'name': equip,
            'original': equip,
            'value': None,
            'group': None
        })

    return result
