from fluxify.transformers import validate_transformation_args


def parot_vi_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None and value != [] and value != {}:
        equipments_temp = value[49].split('|')
        equipments_perso_temp = value[79].split('|')

        for equipment in equipments_temp:
            if type(equipment) is str and equipment != '' and equipment != ' ':
                equipments.append({
                    'name': equipment,
                    'original': equipment,
                    'code': None,
                    'description': None,
                    'price': None
                })

        for equipment in equipments_perso_temp:
            if type(equipment) is str and equipment != '' and equipment != ' ':
                equipments.append({
                    'name': equipment,
                    'original': equipment,
                    'type': 'perso',
                    'code': None,
                    'description': None,
                    'price': None
                })

    return equipments
