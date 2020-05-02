from fluxify.exceptions import ArgumentNotFoundException, InvalidArgumentException


def list_index_exists(data: list, index: int):
    return 0 <= index < len(data)


def validate_transformation_args(transformation: dict):
    if 'value' not in transformation:
        raise ArgumentNotFoundException('"value" argument was not found in transformation mapping.')

    # if 'args' not in transformation:
    #     raise ArgumentNotFoundException('"args" was not found in transformation mapping.')

    # if type(transformation['args']) is not list:
    #     raise InvalidArgumentException('"args" must be an array.')
