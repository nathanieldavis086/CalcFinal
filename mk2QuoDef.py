import random
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, diff, integrate, Pow
from mk1powerindef import power_rule_function


#Works, no touch
def quotient_rule_function():

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
        top = function[:len(function)-1]

    bottom = str(coefficient)
    bottom += "*"
    bottom += 'x'
    bottom += random.choice(operations)
    bottom += str(random.randint(1,10))

    usable_top = parse_expr(top)
    usable_bottom = parse_expr(bottom)
    usable = usable_top * Pow(usable_bottom, -1)

    return usable
    
#quotient_rule_function()


#Works, no touch
def formatQuo():
    x = symbols("x")
    theres_no_way_u_screw_up_that_bad = quotient_rule_function()
    ans = diff(theres_no_way_u_screw_up_that_bad, x)
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + "\n\nProblem: find f'(x) and simplify" + "\n\nAnswer: "
    out = output_format + str(ans) + "\n"

    return out

#formatQuo()


#Works, no touch
def formatDef():
    x = symbols('x')
    theres_no_way_u_screw_up_that_bad = power_rule_function()
    bound1 = random.randint(-10, 0)
    bound2 = random.randint(1,10)
    ans = integrate(theres_no_way_u_screw_up_that_bad, (x, bound1, bound2))
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + "\n\nProblem: integrate f(x) from " + str(bound1) + " to " + str(bound2) + " and simplify" + "\n\nAnswer: "
    out = output_format + str(ans) + "\n"

    return out

#formatDef()