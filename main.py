#POWER RULE DERIVATIVES N REVERSE POWER RULE FOR INTEGRALS(W/O BOUNDS)
from mk1powerindef import formatPow, formatInt
from mk2QuoDef import formatQuo, formatDef

#works but gotta add choices for types of derivatives/integrals, shouldnt be too hard bc of sympy so powerful(im a simp for sympy)

print("Hi there! Let's do some calculus.")


def main():


    calc_type = input("Would you like to practice taking derivatives or taking integrals? Press d for derivatives or i for integrals ")
    print("Note: one asterisk, *, means multiplication, and two, **, means exponent.")
    
    
    
    if calc_type.lower() == "d":
        der_type = input("Would you like to practice power rule or quotient rule? Press p for power or q for quotient")

        if der_type.lower() == "p":
            print(formatQuo())

        elif der_type.lower() == "q":
            print(formatPow())
        
        else:
            print("Error. Please enter p for power rule or q for quotient rule.")
            main()






    elif calc_type.lower() == "i":
        int_type = input("Would you like to practice definite or indefinite integrals (with or without bounds)? Press d for definite or i for indefinite")

        if int_type.lower() == "d":
            print(formatDef())
        
        elif int_type.lower() == "i":
            print(formatInt)
        else:
            print("Error. Please enter d for definite or i for indefinite integrals")
            main()
        



    else:
        print("Error. Please enter d for derivatives or i for integrals.")
        main()

main()