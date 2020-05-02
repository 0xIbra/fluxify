from fluxify.transformers import validate_transformation_args


def str_to_bool(transformation):
    validate_transformation_args(transformation)

    keywords = {
        'VRAI': True,
        'FAUX': False,
        'OUI': True,
        'NON': False,
        'YES': True,
        'NO': False,
        'Y': True,
        'N': False,
        'O': True,
        '1': True,
        '0': False
    }

    value = transformation['value']
    if type(value) is bool:
        return value

    if str(value).upper() in keywords:
        value = keywords[str(value).upper()]

    return value
