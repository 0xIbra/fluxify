from imperium.evaluator import Expression
import re

def test(condition, subject):
    expr = Expression()

    return expr.evaluate(condition, subject)

def handle_conditions(conditions, subject):
    for cond in conditions:
        if not 'condition' in cond:
            raise Exception('Condition is not valid.')

        print(test(cond['condition'], subject))
        exit()

        if test(cond['condition'], subject):
            pass
        else:
            pass