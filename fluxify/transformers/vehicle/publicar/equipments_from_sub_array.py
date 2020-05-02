from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def publicar_equipments_from_sub_array(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"keyToUse" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    key_to_use = transformation['args'][0]
    equipments = []

    if value is not None and type(value) is list:
        for item in value:
            has_tag = item.find(key_to_use)
            if has_tag is None:
                continue

            equipments.append({
                'name': has_tag.text,
                'original': has_tag.text,
                'value': None,
                'group': None
            })

    return equipments
