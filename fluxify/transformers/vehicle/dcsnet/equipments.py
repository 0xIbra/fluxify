from fluxify.transformers import validate_transformation_args


def dcsnet_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []
    equipment_cols = []

    for i in range(81, 110):
        equipment_cols.append(i)

    for col in equipment_cols:
        try:
            name = value[col]

            equipments.append({
                'name': name,
                'original': name,
                'value': None,
                'group': None
            })
        except:
            pass

    return equipments
