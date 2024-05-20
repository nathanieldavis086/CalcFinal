import sympy
import random
from sympy.parsing.sympy_parser import parse_expr
from math import pi

def trig_function():
    x = sympy.symbols('x')
    chooser = random.randint(1,3)
    if chooser == 1:
        return sympy.cos(x)
    elif chooser == 2:
        return sympy.sin(x)
    else:
        return sympy.tan(x)
#trig_function()



def formatIntTrig():
    theres_no_way_u_screw_up_that_bad = trig_function()
    x = sympy.symbols('x')
    ans = sympy.integrate(theres_no_way_u_screw_up_that_bad, x)
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + '\n\nProblem: integrate and simplify f(x)' + '\n\nAnswer: '
    output = output_format + str(ans)

    return output

#formatIntTrig()



def formatDerTrig():

    theres_no_way_u_screw_up_that_bad = trig_function()
    x = sympy.symbols('x')
    ans  = sympy.diff(theres_no_way_u_screw_up_that_bad, x)
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + '\n\nProblem: derive and simplify f(x)' + '\n\nAnswer: '
    output = output_format + str(ans) + "\n"

    return output

#formatDerTrig()


#Works, no touch
def formatIntTrigDef():
    theres_no_way_u_screw_up_that_bad = trig_function()
    x = sympy.symbols('x')
    unit = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6, 2*pi]
    bound1 = random.choice(unit)
    bound2 = random.choice(unit)
    ans = sympy.integrate(theres_no_way_u_screw_up_that_bad, (x, bound1, bound2))
    output_format = '\n\nFunction: f(x) = ' + str(theres_no_way_u_screw_up_that_bad) + '\n\nProblem: integrate f(x) from ' + str(bound1) + " to " + str(bound2) + "\nCalculate in radians" + '\n\nAnswer: '
    out = output_format + str(ans) + "\n"

    return out

#formatIntTrigDef()