def apply_value(item, key, value):
    newitem = current = item
    levels = key.split('.')
    for index, level in enumerate(levels):
        if index + 1 == len(levels):
            current[level] = value
        else:
            current[level] = {}
            
        current = current[level]

    return newitem