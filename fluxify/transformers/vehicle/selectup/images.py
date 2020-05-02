from fluxify.transformers import validate_transformation_args


def selectup_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is not None:
        for img in value:
            if type(img) is str:
                images.append(img)
            elif isinstance(img, object):
                images.append(img.text)

    return images
