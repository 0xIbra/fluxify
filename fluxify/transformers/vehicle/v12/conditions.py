from fluxify.transformers import validate_transformation_args


def v12_conditions(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    result = 'vo'

    if value == '1':
        result = 'vo'
    elif value == '2' or value == '3':
        result = 'vn'

    return result
