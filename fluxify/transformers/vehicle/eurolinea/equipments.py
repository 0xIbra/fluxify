from fluxify.transformers import validate_transformation_args


def eurolinea_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None:
        equipments_temp = value.split(',')

        for equip in equipments_temp:
            name = equip.strip()

            equipments.append({
                'name': name,
                'original': name,
                'value': None,
                'group': None
            })

    return equipments
