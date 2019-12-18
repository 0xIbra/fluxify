from transformers.split import split
from transformers.number import number
from transformers.date import date

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