import math

def main():
    
    print("This program will print prime numbers till you want.")
    choice = input("Do you want to see the first prime number?")
        
    prime_num = generatePrime()
    
    while choice.lower() == "yes" or choice.lower() == "y": #As long as the user wants, the next prime will be generated.
        print(next(prime_num))
        choice = input("And the next?")
    else:
        print("Okay, thank you!")
        
def generatePrime():
    '''
    Will yield the next prime number. 
    '''
    yield 2 #Taking care of 2 separately.
    for num in range (3,100000,2):
        for factor in range(3, int(math.sqrt(num))+1,2):
            if num % factor == 0: 
                break
        else:
            yield num
    
if __name__ == '__main__':
    main()
