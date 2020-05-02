from fluxify.transformers import validate_transformation_args


def publicar_options_from_array(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None:
        for opt in value:
            options.append({
                'name': opt,
                'original': opt,
                'code': None,
                'description': None,
                'price': None
            })

    return options
