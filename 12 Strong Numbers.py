def main():
		
	print("This program generates strong numbers!\n\n")
	ans = input("Do you know what strong numbers are?\n(Enter 'y' or 'n')\n\t")
	if ans.lower() == 'y':
	    print("Okay, cool!")
	else: 
	    print("NOTE: A strong number is defined as that number whose sum of the factorials of the digits equals to the original number itself.")
	    print("For instance: 145 = 1!+4!+5! = 1+24+120")

	lower_lt, upper_lt = map(int, input("\nEnter the lower and upper limit\nwithin which you want your strong numbers to lie:\n\t").split())
	count = 0
	print("\nStrong numbers spotted are:\n")

	for num in range(lower_lt, upper_lt+1):
	    digit_list = list(str(num)) #Integers are not iterables. Thus, first converting a number to a string and then making a list of digits.
	    for digit in range(len(digit_list)):
	    	digit_list[digit] = factorial(int(digit_list[digit]))
	    if num == sum(digit_list):
	    	print(num)
			count += 1
	if count == 0:
		print(f"Sorry no strong number found in the range {lower_lt}-{upper_lt}.")
		
def factorial(num):
	'''
	Will help us to find the factorial of a number.
	Argument:
	num - Integer. The number whose factorial the method will calculate.
	'''
	if num == 1 or num == 0:
		return 1
	return num * factorial(num-1)

if __name__ == '__main__':
	main()