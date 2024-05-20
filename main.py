#POWER RULE DERIVATIVES N REVERSE POWER RULE FOR INTEGRALS(W/O BOUNDS)
from mk1powerindef import formatPow, formatInt
from mk2QuoDef import formatQuo, formatDef
from mk3trig import formatDerTrig, formatIntTrig, formatIntTrigDef



print("\n\n\n\nHi there! Let's do some calculus.\n")


def main():


    calc_type = input("Would you like to practice taking derivatives or taking integrals? Press d for derivatives or i for integrals: ")
    print("\nNote: one * means multiplication, and ** means exponent.\n")
    
    
    
    if calc_type.lower() == "d":
        der_type = input("Would you like to practice power rule, quotient rule or trig functions? Press p for power, q for quotient, or t for trig: ")


        if der_type.lower() == "q":
            print(formatQuo())

        elif der_type.lower() == "p":
            print(formatPow())

        elif der_type.lower() == "t":
            print(formatDerTrig())
        
        else:
            print("Error. Please enter p for power rule, q for quotient rule, or t for trig.")
            return






    elif calc_type.lower() == "i":
        int_type = input("Would you like to practice definite or indefinite integrals (with or without bounds)? Press d for definite or i for indefinite: ")


        if int_type.lower() == "d":
            trigOrNo = input("Would you like to do trig or regular? Press t for trig or r for regular: ")

            if trigOrNo.lower() == 'r':
                print(formatDef())
            
            elif trigOrNo.lower() == "t":
                print(formatIntTrigDef())
            else:
                print("Error. Please enter t for trig or r for regular")
                return

        
        elif int_type.lower() == "i":
            trigOrNot = input("Would you like to do trig or regular? Press t for trig or r for regular: ")

            if trigOrNot.lower() == 'r':
                print(formatInt())

            elif trigOrNot.lower() == 't':
                print(formatIntTrig())
            else:
                print("Error. Please enter t for trig or r for regular")
                return



        else:
            print("Error. Please enter d for definite or i for indefinite integrals: ")
            return
        



    else:
        print("Error. Please enter d for derivatives or i for integrals.")
        return

main()