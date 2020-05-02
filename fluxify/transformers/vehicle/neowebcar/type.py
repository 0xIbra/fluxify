from fluxify.transformers import validate_transformation_args


def neowebcar_type(transformation: dict):
    validate_transformation_args(transformation)

    value = int(transformation['value'])

    if value == 0:
        type_value = 'vp'
    elif value == 1:
        type_value = 'vu'
    elif value == 2:
        type_value = 'vs'
    else:
        type_value = None

    return type_value
