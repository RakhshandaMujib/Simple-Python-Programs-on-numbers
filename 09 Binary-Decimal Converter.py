import math

def main():
    print("This program will conver binary to decimal and decimal to binary.\n\n\ta) Convert binary to decimal \tb) Convert decimal to binary")
    choice = input("\nEnter choice:\t")
    number = int(input("Enter the number you want to convert:\t"))
    if choice == "a":
        binary = number
        
        #Checking if the number entered is actually a binary number or not.
        bin_set = {'0','1'}
        str_bin_set = set(str(binary))
        if str_bin_set == bin_set or str_bin_set == {'0'} or str_bin_set == {'1'}: #Number is a binary number.
            print(f"The decimal number for {binary} is:\n{binToDeci(binary)}")
        else: 
            print("Invalid number entered.")
    elif choice == "b":
        decimal = number
        print(f"The decimal number for {decimal} is:\n{deciToBin(decimal)}")
    else:
        print("Invalid choice entered!")
    
def binToDeci(num):
    '''
    This method converts a binary number to its decimal form. 
    Arguments:
    num - int, the binary number that the method converts to decimal.
    '''
    power = 0
    deci_no = 0
    while num != 0:
        deci_no += (num%10)*(2**power)
        num = round(num/10)
        power += 1
    return deci_no

def deciToBin(num):
    '''
    This method converts a binary number to its decimal form. 
    Arguments:
    num - int, the decimal number that the method converts to binary.
    '''
    bin_no_list = []
    if num == 0 or num == 1: #Taking care of 0 and 1 separately. 
        return num
    else: 
        while num!= 1:
            bin_no_list.append(num%2) #Appending the remainders to the list.
            num = math.floor(num/2)

        bin_no_list.append(1) #Adding the first 1. 
        bin_no_list.reverse() #The original list is created in the reverse order. So, reversing the list to get the needed list.
        
        #Converting list to int:
        str_bin_no_list = [str(digit) for digit in bin_no_list] 
        bin_no = int("".join(str_bin_no_list))
        
        return bin_no
        
        
if __name__ == '__main__':
    main()