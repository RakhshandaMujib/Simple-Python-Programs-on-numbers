def main():

    print("This program generates special numbers!\n\n")
    ans = input("Do you know what special numbers are?\n(Enter 'y' or 'n')\n\t")
    if ans.lower() == 'y':
        print("Okay, cool!")
    else: 
        print("NOTE: A special number is defined as that number whose sum of the sum and product of the digits equals to the original number itself.")
        print("For instance: 99 = (9+9)+(9*9) = 18+81")

    lower_lt, upper_lt = map(int, input("\nEnter the lower and upper limit\nwithin which you want your special numbers to lie:\n\t").split())
    count = 0 #For counting the number of successful results.
    product = 1
    
    print("Special numbers spotted are:\n")
    for num in range(lower_lt,upper_lt+1):
        digit_list = list(str(num)) #Integers are not iterables. 
                                    #Thus, first converting the number to a string and then making a list its digits.
        for index in range(len(digit_list)):
            digit_list[index] = int(digit_list[index]) #Coverting the digits from strings to integers.
            product *= digit_list[index]
        if sum(digit_list) + product == num:
            print(num)
            count += 1
        product = 1
    
    if count == 0:
        print(f"Sorry, no special numbers found in range {lower_lt}-{upper_lt}.")


if __name__ == '__main__':
    main()