from imperium.evaluator import Expression
import re, parser

def test(condition, subject):
    expr = Expression()

    return expr.evaluate(condition, subject)

def normalize(value):
    if value == 'true':
        return True
    if value == 'false':
        return False

    return value

def has(key, subject):
    split = key.split('.')
    for Key in split:
        if Key == '$subject':
            continue

        if not Key in subject:
            return False
        
        subject = subject[Key]

    return True

def get(key, subject):
    split = key.split('.')
    for Key in split:
        if Key == '$subject':
            continue

        if not Key in subject:
            return False
        
        subject = subject[Key]

    return subject


def handle_conditions(conditions, subject):
    returnvalue = False
    for cond in conditions:
        if not 'condition' in cond:
            raise Exception('Condition is not valid.')

        if test(cond['condition'], subject):
            value = normalize(cond['returnOnSuccess'])
            if type(value) == str and '$subject.' in value:
                value = get(value, subject)
            if type(value) == str and '$subject[' in value:
                value = value.replace('$subject', 'subject')
                expr = parser.expr(value)

                value = eval(expr.compile(''))

            returnvalue = value
        else:
            value = normalize(cond['returnOnFail'])
            if type(value) == str and '$subject' in value:
                value = get(value, subject)
            
            returnvalue = value
    
    return returnvalue