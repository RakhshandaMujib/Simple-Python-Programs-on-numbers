import math

def main():
	'''
	The user can perform simple operations like add, subtract, multiply & divide and find exponents of numbers as well.
	'''
    print("This is a simple calculator.\n(Please use parentheses wherever needed.)")
    expression = input("Enter expression:\n") #Use '**' for exponents. 
    print(eval(expression)) #The eval() method calculates the mathematical value of the expression entered by the user.
    
if __name__ == '__main__':
    main()