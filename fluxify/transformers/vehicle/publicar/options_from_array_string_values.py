from fluxify.transformers import validate_transformation_args, list_index_exists
from fluxify.exceptions import ArgumentNotFoundException


def publicar_options_from_array_string_values(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"delimiter" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['args'][0]
    options = []

    if value is not None:
        options_temp = value.split(delimiter)

        for opt in options_temp:
            if str(opt).strip() == '':
                continue

            options.append({
                'name': opt,
                'original': opt,
                'code': None,
                'description': None,
                'price': None
            })

    return options
