from fluxify.exceptions import ArgumentNotFoundException
from fluxify.transformers import list_index_exists, validate_transformation_args


def starterre_images(transformation: dict):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"delimiter" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    delimiter = transformation['args'][0]
    max_number = None
    if list_index_exists(transformation['args'], 1):
        max_number = int(transformation['args'][1])

    images = []

    if value is not None and type(value) is str:
        img_list = value.split(delimiter)

        if max_number is not None:
            for i in range(max_number):
                images.append(img_list[i])
        else:
            images = img_list

    return images
