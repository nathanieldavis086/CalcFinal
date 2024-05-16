import random
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
from sympy import diff, integrate
from mk1powerindef import power_rule_function


x = symbols("x")
def quotient_rule_function():
    coefficient_new = power_rule_function.coefficient
    bottom_operations = ["+","-"]

    top = power_rule_function()
    bottom = str(coefficient_new)
    bottom += "x"
    bottom += random.choice(bottom_operations)
    bottom += str(coefficient_new)

    real = str(top) + "/" + str(bottom)

    return parse_expr(real)
    
quotient_rule_function()






def formatQuo():
    ans = diff(quotient_rule_function(),x)
    out = '\nFunction: f(x) = ' + str(quotient_rule_function()) + "\n\nProblem: find f'(x) and simplify" + "\n\nAnswer: " + ans
    return out

formatQuo()

def formatDef():
    bound1 = random.randint(-10,10)
    bound2 = random.randint(-10,10)
    ans = integrate(power_rule_function(), x, bound1, bound2)
    out = '\nFunction: f(x) = ' + str(quotient_rule_function()) + "\n\nProblem: integrate " + power_rule_function() + " from " + bound1 + " to " + bound2 + " and simplify" + "\n\nAnswer: " + ans
    return out
formatDef()