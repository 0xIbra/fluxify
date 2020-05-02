from fluxify.transformers import validate_transformation_args


def number(transformation):
    validate_transformation_args(transformation)

    value = transformation['value']

    if type(value) == int or type(value) == float:
        return value

    if ',' in value and type(value) is str:
        value = value.replace(',', '.')
    
    if '.' in value and type(value) is str:
        value = float(value)
    else:
        value = int(value)

    return value
