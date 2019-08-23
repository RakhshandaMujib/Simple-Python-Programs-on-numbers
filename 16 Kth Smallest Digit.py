def main():
	k = int(input("Enter the value of k:\t"))
	list_is = input("Enter the numbers in your list (separated by spaces):\n").split()
	list_is = [int(item) for item in list_is]
	if k > len(set(list_is)):
		print(f"{k} is greater than the number of unique digits entered.")
	else:
		print(f"The {k}th smallest digit is: \n\t{sorted(set(list_is))[k-1]}")
		
if __name__ == '__main__':
	main()
