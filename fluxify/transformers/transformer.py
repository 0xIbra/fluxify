from fluxify.transformers.split import split
from fluxify.transformers.number import number
from fluxify.transformers.date import date
from fluxify.transformers.replace import replace
from fluxify.transformers.boolean import boolean
from fluxify.transformers.custom import equipments_from_string, options_from_string
from fluxify.exceptions import UnsupportedTransformerException

TRANSFORMERS = {
    'number': number,
    'split': split,
    'date': date,
    'replace': replace,
    'boolean': boolean,
    'equipments_from_string': equipments_from_string,
    'options_from_string': options_from_string
}

def handle_transformations(transformations, value):
    finalvalue = value
    for transformation in transformations:
        transformation['value'] = finalvalue
        transformer = transformation['transformer']
        if not transformer in TRANSFORMERS:
            raise UnsupportedTransformerException('Unsupported transformer: "{}"'.format(transformer))

        invoker = TRANSFORMERS[transformer]
        finalvalue = invoker(transformation)

    return finalvalue