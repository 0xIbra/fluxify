from fluxify.transformers import validate_transformation_args, list_index_exists
from fluxify.exceptions import ArgumentNotFoundException


def vulcain_images(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"delimiter" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['args'][0]
    images = []

    out = value[71].split(delimiter)

    if out is not None:
        for item in out:
            if type(item) is str:
                images.append(f'{value[0]}-VO-{item}')

    return images
