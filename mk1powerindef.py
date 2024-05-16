import random
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
from sympy import diff, integrate

x = symbols('x')
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

    usable_function = parse_expr(function[0:len(function)-1])
    

    return usable_function
power_rule_function()



def formatInt():
    #USE CLASSES IMP
    #  File "/Users/apple/Desktop/RealCS/mathgenprob.py", line 40, in <module>
    #format()
    #TypeError: format() missing 1 required positional argument: 'ans'
    #gotta find how to run this format correctly with the answer, or maybe just leave the answer out of this function
    #and add it on its own line in main
    #also, need to figure out what returning something does when the function its in gets called in main
    #seems like it runs it before anything else in main, but its in the air

    #IMP when coding answer into format (as a string) don't forget to put a new line after the answer
    output_format = '\nFunction: f(x) = ' + str(power_rule_function()) + '\n\nProblem: integrate and simplify f(x)' + '\n\nAnswer: '
    intans = integrate(power_rule_function(),x)
    intOut = output_format + str(intans) + "\n"
    return intOut
    
formatInt()


def formatPow():
    #USE CLASSES IMP
    #  File "/Users/apple/Desktop/RealCS/mathgenprob.py", line 40, in <module>
    #format()
    #TypeError: format() missing 1 required positional argument: 'ans'
    #gotta find how to run this format correctly with the answer, or maybe just leave the answer out of this function
    #and add it on its own line in main
    #also, need to figure out what returning something does when the function its in gets called in main
    #seems like it runs it before anything else in main, but its in the air

    n = random.randint(1,3)
    dashes = "\'"*n
    #IMP when coding answer into format (as a string) don't forget to put a new line after the answer
    output_format = '\nFunction: f(x) = ' + str(power_rule_function()) + '\n\nProblem: find f'+(dashes) + '(x) and simplify the answer' + '\n\nAnswer: '
    derans = diff(power_rule_function(), x, n)
    derOut = output_format + str(derans)+ "\n"
    return derOut
    
formatPow()