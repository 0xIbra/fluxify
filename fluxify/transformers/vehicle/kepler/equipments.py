from fluxify.transformers import validate_transformation_args


def kepler_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None and value is not False:
        if type(value) is list:
            for equip in value:
                name = None
                name_tag = equip.find('name')
                if name_tag is not None:
                    name = name_tag.text

                if name is not None:
                    equipments.append({
                        'name': name,
                        'original': name,
                        'value': None,
                        'group': None,
                        'type': None
                    })
        else:
            try:
                name = None
                name_tag = value.find('name')
                if name_tag is not None:
                    name = name_tag.text

                if name is not None:
                    equipments.append({
                        'name': name,
                        'original': name,
                        'value': None,
                        'group': None,
                        'type': None
                    })
            except:
                pass

    return equipments
