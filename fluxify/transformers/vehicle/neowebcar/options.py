from fluxify.transformers import validate_transformation_args


def neowebcar_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None and isinstance(value, object):
        value = [value]

    if type(value) is list:
        for item in value:
            name = None
            code = None
            description = None
            price = None

            name_tag = item.find('name')
            if name_tag is not None:
                name = name_tag.text

            mpn_tag = item.find('mpn')
            if mpn_tag is not None:
                code = mpn_tag.text

            desc_tag = item.find('description')
            if desc_tag is not None:
                description = desc_tag.text

            price_tag = item.find('price')
            if price_tag is not None:
                price = float(price_tag.text)

            options.append({
                'name': name,
                'original': name,
                'code': code,
                'description': description,
                'price': price
            })

    return options
