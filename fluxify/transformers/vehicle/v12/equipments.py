from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def v12_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    if value is not None:
        for item in value:
            name = item.text
            attributes = item.attrib

            if 'type' in attributes:
                type_attr = int(attributes['type'])
                if type_attr == 1 or type_attr == 2 or type_attr == 3:
                    value = None
                    if 'id' in attributes:
                        value = attributes['id']

                    equip_type = None
                    if type_attr == 3 or type_attr == 4:
                        equip_type = 'pack'

                    group = None
                    if 'group' in attributes:
                        group = attributes['group']

                    equipments.append({
                        'name': name,
                        'original': name,
                        'value': value,
                        'type': equip_type,
                        'group': group
                    })

    return equipments
