from fluxify.transformers.split import split
from fluxify.transformers.number import number
from fluxify.transformers.date import date

TRANSFORMERS = {
    'number': number,
    'split': split,
    'date': date
}

def handle_transformations(transformations, value):
    finalvalue = value
    for transformation in transformations:
        transformation['value'] = finalvalue
        transformer = transformation['transformer']
        invoker = TRANSFORMERS[transformer]
        finalvalue = invoker(transformation)

    return finalvalue