from fluxify.transformers import validate_transformation_args


def parot_vi_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None and value != {} and value != []:
        options_temp = value[48].split('|')
        options_perso_temp = value[78].split('|')

        for opt in options_temp:
            options.append({
                'name': opt,
                'original': opt,
                'code': None,
                'description': None,
                'price': None
            })

        for opt in options_perso_temp:
            options.append({
                'name': opt,
                'original': opt,
                'type': 'perso',
                'code': None,
                'description': None,
                'price': None
            })

    return options
