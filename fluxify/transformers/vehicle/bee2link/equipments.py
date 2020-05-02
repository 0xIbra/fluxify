from fluxify.transformers import validate_transformation_args


def bee2link_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if type(value) is list:
        for equip in value:
            name = None
            libelle_tag = equip.find('LIBELLE')
            if libelle_tag is not None:
                name = libelle_tag.text

            equip_type = None
            if 'type' in equip.attrib:
                equip_type = equip.attrib['type']

            if name is not None and equip_type is not None and int(equip_type) == 1:
                equipments.append({
                    'name': name,
                    'original': name,
                    'value': None,
                    'group': None,
                    'type': None
                })
    else:
        name = None
        libelle_tag = value.find('LIBELLE')
        if libelle_tag is not None:
            name = libelle_tag.text

        equip_type = None
        if 'type' in value.attrib:
            equip_type = value.attrib['type']

        if name is not None and equip_type is not None and int(equip_type) == 1:
            equipments.append({
                'name': name,
                'original': name,
                'value': None,
                'group': None,
                'type': None
            })

    return equipments
