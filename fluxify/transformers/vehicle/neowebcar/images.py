from fluxify.transformers import validate_transformation_args
import os


def neowebcar_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is not None and type(value) is not list:
        value = [value]

    if value is not None:
        for path in value:
            images.append(os.path.join('http://static.neowebcar.com', path))

    return images
