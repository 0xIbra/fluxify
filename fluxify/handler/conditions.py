from imperium.evaluator import Expression
from fluxify.exceptions import ConditionNotFoundException
import re, parser


def test(condition, subject, source=None):
    expr = Expression()

    return expr.evaluate(condition, subject, source)


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


def handle_conditions(conditions, subject, source=None):
    returnvalue = False
    for cond in conditions:
        if not 'condition' in cond:
            raise ConditionNotFoundException('key "condition" was not found in mapping.')

        if test(cond['condition'], subject=subject, source=source):
            value = normalize(cond['returnOnSuccess'])
            if type(value) == str and '$subject.' in value:
                value = get(value, subject)

            if type(value) == str and '$subject[' in value:
                value = value.replace('$subject', 'subject')
                expr = parser.expr(value)

                value = eval(expr.compile(''))

            if type(value) == str and '$source[' in value:
                value = value.replace('$source', 'source')
                expr = parser.expr(value)

                value = eval(expr.compile(''))

            return value
        else:
            if not 'returnOnFail' in cond:
                cond['returnOnFail'] = False

            value = normalize(cond['returnOnFail'])
            if type(value) == str and '$subject.' in value:
                value = get(value, subject)

            if type(value) == str and '$subject[' in value:
                value = value.replace('$subject', 'subject')
                expr = parser.expr(value)

                value = eval(expr.compile(''))

            if type(value) == str and '$source[' in value:
                value = value.replace('$source', 'source')
                expr = parser.expr(value)

                value = eval(expr.compile(''))

            returnvalue = value
    
    return returnvalue
