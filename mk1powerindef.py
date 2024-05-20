import random
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
from sympy import diff, integrate

#ALL 3 METHODS WORK, DONT FUCK W IT

#POWER RULE FUNCTION GENERATOR
def power_rule_function():
    i=0
    function = ""
    numOfTerms = random.randint(1,5)

    while (i<numOfTerms):

        i+=1

        power_num = random.randint(1,5)
        coefficient = random.randint(1,10)
        operations = ["+", "-"]
        function += str(coefficient)
        function += "*"
        function += "x"
        function += "**"
        function += str(power_num)
        function += random.choice(operations)

    real = function[0:len(function)-1]
    usable_function = parse_expr(real)

    return usable_function

#power_rule_function()


#Works, no touch
def formatInt():
    
    x = symbols('x')
    theres_no_way_u_screw_up_that_bad = power_rule_function()
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + '\n\nProblem: integrate and simplify f(x)' + '\n\nAnswer: '
    ans = integrate(theres_no_way_u_screw_up_that_bad,x)
    out = output_format + str(ans) + "\n"

    return out
    
#formatInt()

#Works, no touch
def formatPow():
    
    x = symbols('x')
    theres_no_way_u_screw_up_that_bad = power_rule_function()
    n = random.randint(1,3)
    dashes = "\'"*n
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + '\n\nProblem: find f'+(dashes) + '(x) and simplify the answer' + '\n\nAnswer: '
    derans = diff(theres_no_way_u_screw_up_that_bad, x, n)
    out = output_format + str(derans)+ "\n"

    return out

#formatPow()