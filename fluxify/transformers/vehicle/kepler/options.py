from fluxify.transformers import validate_transformation_args


def kepler_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None:
        if type(value) is list:
            for opt in value:
                name = None
                price = None

                name_tag = opt.find('name')
                if name_tag is not None:
                    name = name_tag.text

                price_tag = opt.find('price')
                if price_tag is not None:
                    price = price_tag.text

                if name is not None:
                    options.append({
                        'name': name,
                        'original': name,
                        'price': price,
                        'value': None,
                        'group': None,
                        'type': None
                    })
        else:
            try:
                name = None
                price = None

                name_tag = value.find('name')
                if name_tag is not None:
                    name = name_tag.text

                price_tag = value.find('price')
                if price_tag is not None:
                    price = price_tag.text

                if name is not None:
                    options.append({
                        'name': name,
                        'original': name,
                        'price': price,
                        'value': None,
                        'group': None,
                        'type': None
                    })
            except:
                pass

    return options
