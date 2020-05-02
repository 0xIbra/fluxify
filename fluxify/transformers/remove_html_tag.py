from fluxify.exceptions import ArgumentNotFoundException, InvalidArgumentException
from fluxify.transformers import list_index_exists, validate_transformation_args


def remove_html_tag(transformation):
    validate_transformation_args(transformation)

    if not list_index_exists(transformation['args'], 0):
        raise ArgumentNotFoundException('"tags" (index: 0) argument was not found in transformation mapping.')

    value = transformation['value']
    tags = transformation['args'][0]

    if type(tags) is not list:
        raise InvalidArgumentException('"tags" (index: 0) argument must be of type array/list. {} given.'
                                       .format(str(type(tags))))

    for tag in tags:
        opening_tag = f'<{tag}>'
        closing_tag = f'</{tag}>'

        value = str(value).replace(opening_tag, ' ')
        value = value.replace(closing_tag, ' ')
        value = value.replace('  ', ' ')

    return value.strip()
