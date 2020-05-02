from fluxify.transformers import validate_transformation_args


def auto123_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is None or value == {} or value == []:
        return equipments

    if 'OptionName' in value:
        equipments.append({
            'name': value['OptionName'][0],
            'original': value['OptionName'][0],
            'value': None,
            'group': None
        })
    else:
        for arr in value:
            cur = arr['OptionName'][0]

            if type(cur) is str:
                str_value = cur
            else:
                str_value = cur[0]

            equipments.append({
                'name': str_value,
                'original': str_value,
                'value': None,
                'group': None
            })

    return equipments
