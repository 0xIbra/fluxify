from fluxify.transformers import validate_transformation_args
import re


def vulcain_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None:
        equipments_temp = value.split('|')

        for string in equipments_temp:
            name = str(string).strip()

            equip_temp = re.split('##', name)

            equipments.append({
                'name': equip_temp[1],
                'original': equip_temp[1],
                'value': equip_temp[0],
                'group': None
            })

    return equipments
