from fluxify.transformers.split import split
from fluxify.transformers.number import number
from fluxify.transformers.date import date
from fluxify.transformers.replace import replace
from fluxify.transformers.boolean import boolean
from fluxify.transformers.custom import equipments_from_string, options_from_string
from fluxify.exceptions import UnsupportedTransformerException, InvalidArgumentException, ArgumentNotFoundException, ConditionNotFoundException

TRANSFORMERS = {
    'number': number,
    'split': split,
    'date': date,
    'replace': replace,
    'boolean': boolean,
    'equipments_from_string': equipments_from_string,
    'options_from_string': options_from_string
}


def handle_transformations(transformations, value, error_tolerance=False):
    finalvalue = value
    for transformation in transformations:
        transformation['value'] = finalvalue
        transformation['error_tolerance'] = error_tolerance
        transformer = transformation['transformer']
        if not transformer in TRANSFORMERS:
            raise UnsupportedTransformerException('Unsupported transformer: "{}"'.format(transformer))

        invoker = TRANSFORMERS[transformer]
        if error_tolerance:
            try:
                finalvalue = invoker(transformation)
            except (InvalidArgumentException, ArgumentNotFoundException, ConditionNotFoundException, UnsupportedTransformerException, Exception) as e:
                print('[warning] ', e)
        else:
            finalvalue = invoker(transformation)

    return finalvalue
