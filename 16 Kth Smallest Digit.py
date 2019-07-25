def main():
	k = int(input("Enter the value of k:\t"))
	print("Enter the numbers in your list: (Enter any alphabet to stop)")
	list_is = []
	while True:
		element = input("\t")
		if element.lower().isalpha():
			break
		else:
			list_is.append(int(element))
	print(f"The elements are:\n\t{list_is}")

	if k > len(set(list_is)):
		print(f"{k} is greater than the number of unique digits entered.")
	else:
		print(f"The {k}th smallest digit is: \n\t{sorted(set(list_is))[k-1]}")
		
if __name__ == '__main__':
	main()