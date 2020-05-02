from fluxify.transformers import validate_transformation_args


def kepler_images(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    images = []

    if value is not None:
        if type(value) is list:
            for item in value:
                photo_tag = item.find('photo')
                if photo_tag is not None:
                    images.append(photo_tag.text)
        else:
            try:
                photo_tag = value.find('photo')
                if photo_tag is not None:
                    images.append(photo_tag.text)
            except:
                pass

    return images
