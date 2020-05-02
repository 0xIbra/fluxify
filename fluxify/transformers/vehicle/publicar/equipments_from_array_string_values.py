from fluxify.transformers import validate_transformation_args, list_index_exists
from fluxify.exceptions import ArgumentNotFoundException


def publicar_equipments_from_array_string_values(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"delimiter" (index: 0) argument was not found transformation mapping.')

    value = transformation['value']
    delimiter = transformation['args'][0]
    equipments = []

    if value is not None:
        equipments_temp = value.split(delimiter)

        for equip in equipments_temp:
            if equip.strip() == '':
                continue

            equipments.append({
                'name': equip,
                'original': equip,
                'value': None,
                'group': None
            })

    return equipments
