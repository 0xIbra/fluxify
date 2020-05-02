from fluxify.transformers import validate_transformation_args


def selectup_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None:
        for equip in value:
            name = None
            if isinstance(equip, object):
                name = equip.text
            elif type(equip) is str:
                name = equip

            if name is not None and type(name) is str:
                if name.strip() != '':
                    equipments.append({
                        'name': name,
                        'original': name,
                        'value': None,
                        'group': None,
                        'type': None
                    })

    return equipments
