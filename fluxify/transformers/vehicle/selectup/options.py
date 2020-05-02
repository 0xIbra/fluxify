from fluxify.transformers import validate_transformation_args


def selectup_options(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    options = []

    if value is not None:
        for opt in value:
            name = None
            name_tag = opt.find('Description')
            if name_tag is not None:
                name = name_tag.text

            description = name

            code = None
            code_tag = opt.find('Code')
            if code_tag is not None:
                code = code_tag.text

            priceht = None
            priceht_tag = opt.find('PrixHT')
            if priceht_tag is not None:
                priceht = priceht_tag.text

            pricettc = None
            pricettc_tag = opt.find('PrixTTC')
            if pricettc_tag is not None:
                pricettc = pricettc_tag.text

            tva = None
            if priceht is not None and pricettc is not None:
                tva = float(pricettc) - float(priceht)

            if name is not None:
                options.append({
                    'name': name,
                    'original': name,
                    'code': code,
                    'description': description,
                    'price': priceht,
                    'tva': tva
                })

    return options
