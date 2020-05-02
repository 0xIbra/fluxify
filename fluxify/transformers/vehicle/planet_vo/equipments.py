from fluxify.transformers import validate_transformation_args


def planet_vo_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if type(value) is str:
        if value.strip() != '':
            for equipment in value.split('|'):
                equipments.append({
                    'name': equipment,
                    'original': equipment,
                    'value': None,
                    'group': None
                })

    return equipments
