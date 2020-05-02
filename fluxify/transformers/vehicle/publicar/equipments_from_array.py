from fluxify.transformers import validate_transformation_args


def publicar_equipments_from_array(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None:
        for equip_str in value:
            equipments.append({
                'name': equip_str,
                'original': equip_str,
                'value': None,
                'group': None
            })

    return equipments
