from fluxify.transformers import validate_transformation_args
import json


def ubiflow_options(transformation: dict):
    validate_transformation_args(transformation)

    options = []
    value = transformation['value']

    if value is not None and value != '' and value != ' ':
        options_temp = json.loads(value)
        for opt in options_temp:
            code = description = price = None

            if type(opt) is dict and 'prix' in opt:
                price = float(opt['prix'])

            options.append({
                'name': opt['libelle'],
                'original': opt['libelle'],
                'code': code,
                'description': description,
                'price': price
            })

    return options
