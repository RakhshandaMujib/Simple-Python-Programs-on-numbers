def main():
    print("This is simple program that helps you to calculate the factorial of a number.")
    num = int(input("Enter a number:\n\t"))
    
    #Use this commented section to work with while loop.
    '''
    fact = 1
    
    if num == 0:
        pass
    else: 
        temp = num
        while temp != 1:
            fact *= temp
            temp -= 1
    '''
    
    fact = find_fact(num) #Comment this line if using the above section. 
    print(f"{num}! = {fact}") 

def find_fact(n):
    '''
    Uses recursion to calculate the factorial.
    Argument:
    n - int. Number the user wants to find the factorial of.  
    '''
    if n == 1 or n == 0:
        return 1
    return n* find_fact(n-1)

if __name__ == '__main__':
    main()