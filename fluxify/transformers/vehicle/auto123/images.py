from fluxify.transformers import validate_transformation_args


def auto123_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is None:
        return images

    if value == {} or value == []:
        return images

    if 'Filename' in value:
        images.append(value['Filename'][0])
    else:
        for arr in value:
            images.append(arr[0]['Filename'][0])

    return images
