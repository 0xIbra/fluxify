from fluxify.exceptions import ArgumentNotFoundException, InvalidArgumentException


def boolean(transformation):
    if not 'value' in transformation:
        raise ArgumentNotFoundException('[transformation][replace] "value" argument was not found in transformation mapping.')

    if type(transformation['value']) != str:
        raise InvalidArgumentException('[transformation][replace] "value" argument must be a string for replace')

    value = str(transformation['value']).lower()
    if type(value) == str and value == 'true':
        value = True

    if type(value) == str and value == 'false':
        value = False

    if type(value) == str and value.isdigit():
        value = int(value)

    return bool(value)
