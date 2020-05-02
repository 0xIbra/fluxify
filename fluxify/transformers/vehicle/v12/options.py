from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def v12_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None:
        for item in value:
            name = item.text
            attributes = item.attrib

            if 'type' in attributes:
                type_attr = int(attributes['type'])
                if type_attr == 2:
                    code = None
                    if 'code' in attributes:
                        code = attributes['code']

                    description = None
                    if 'description' in attributes:
                        description = attributes['description']

                    price = None
                    if 'price' in attributes:
                        price = attributes['price']

                    tva = None
                    if 'tva' in attributes:
                        tva = attributes['tva']

                    options.append({
                        'name': name,
                        'original': name,
                        'code': code,
                        'description': description,
                        'price': price,
                        'tva': tva
                    })

    return options
