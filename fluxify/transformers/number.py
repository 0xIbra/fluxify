def number(transformation):

    value = transformation['value']

    if type(value) == int or type(value) == float:
        return value

    if ',' in value and type(value) is str:
        value = value.replace(',', '.')
    
    if '.' in value and type(value) is str:
        value = float(value)
    else:
        value = int(value)

    return value
