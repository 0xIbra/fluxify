from fluxify.transformers import validate_transformation_args


def edp_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is not None:
        for item in value:
            images.append(item.attrib['url'])

    return images
