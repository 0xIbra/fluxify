from fluxify.transformers import validate_transformation_args


def eurolinea_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None:
        options_temp = [
            {'name': value[57], 'price': value[58]},
            {'name': value[59], 'price': value[60]},
            {'name': value[61], 'price': value[62]},
            {'name': value[63], 'price': value[64]},
            {'name': value[65], 'price': value[66]},
            {'name': value[67], 'price': value[68]},
        ]

        for opt in options_temp:
            name = str(opt['name']).strip()
            price = str(opt['price']).strip()

            options.append({
                'name': name,
                'original': name,
                'code': None,
                'description': None,
                'price': price,
                'tva': None
            })

    return options
