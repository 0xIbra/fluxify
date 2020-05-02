from fluxify.transformers import validate_transformation_args


def bee2link_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if type(value) is list:
        for opt in value:
            name = None
            libelle_tag = opt.find('LIBELLE')
            if libelle_tag is not None:
                name = libelle_tag.text

            opt_type = None
            if 'type' in opt.attrib:
                opt_type = opt.attrib['type']

            if name is not None and opt_type is not None and int(opt_type) == 2:
                options.append({
                    'name': name,
                    'original': name,
                    'value': None,
                    'group': None,
                    'type': None
                })
    else:
        name = None
        libelle_tag = value.find('LIBELLE')
        if libelle_tag is not None:
            name = libelle_tag.text

        opt_type = None
        if 'type' in value.attrib:
            opt_type = value.attrib['type']

        if name is not None and opt_type is not None and int(opt_type) == 1:
            options.append({
                'name': name,
                'original': name,
                'value': None,
                'group': None,
                'type': None
            })

    return options
