def main():
		
	print("This program generates happy numbers!\n\n")
	ans = input("Do you know what happy numbers are?\n(Enter 'y' or 'n')\n\t")
	if ans.lower() == 'y':
	    print("Okay, cool!")
	else: 
	    print("NOTE: A happy number is defined by the following process.\nStarting with any positive integer,\nreplace the number by the sum of the squares of\nits digits, and repeat the process until\nthe number equals 1 (where it will stay), or it loops\nendlessly in a cycle which does not include 1.\nThose numbers for which this process ends in 1 are happy numbers,\nwhile those that do not end in 1 are unhappy numbers.")

	lower_lt, upper_lt = map(int, input("\nEnter the lower and upper limit\nwithin which you want your happy numbers to lie:\n\t").split())
	count = 0
    
	print("\nHappy number(s) spotted is/are:\n")

	for num in range(lower_lt, upper_lt+1):
	    digit_list = list(str(num)) #Integers are not iterables. Thus, first converting a number to a string and then making a list of digits.
	    while len(digit_list) != 1: #When the sum of squares finally reduces to a single digit.
	        for digit in range(len(digit_list)): 
	            digit_list[digit] = int(digit_list[digit])**2 #Finding the square of each digit in the number list.
	        digit_list = list(str(sum(digit_list))) #Replacing the list of digits with the digits of the sum of squares of the number.
	    if digit_list[0] == '1': #Checking if last sum of squares was equal to 1.
	        print(num) #If it were, then the number was a happy number!
	        count += 1
    
	if count == 0:
	    print("Sorry, no happy numbers found in the range {lower_lt}-{upper_lt}.")

if __name__ == '__main__':
	main()