from fluxify.transformers import validate_transformation_args


def bee2link_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is not None and type(value) is list:
        for img in value:
            if type(img) is str:
                # If raw: True, in this case, img is a string retrieved from the xml tag
                images.append(img)
            else:
                # If raw: False, in this case, img is an etree.Element object
                images.append(img.text)

    return images
