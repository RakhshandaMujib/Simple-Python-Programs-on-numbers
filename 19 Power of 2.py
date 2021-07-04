def main():
	num = int(input('Enter a number: '))

	#Approach: 
	#	Perform bit-wise AND operation on the number and its predecessor. Iff 
	#	the result is 0, the number is a power of 2.
	#Reason:
	#	A number is a power of 2 if its binary representation is of the form 1 
	#	followed by n number of 0's. On performing bit-wise AND operation, we 
	#	necessarily checking if that condition holds true.
	#E.g.:
	#	num = 8 and 8 in binary = 1000
	#	num - 1 = 7 and 7 in binary = 111 or 0111
	#   Now,   1000
	#        & 0111
	#        = 0000 
	if not num & num - 1: 
		print(f'{num} is a power of 2.')
	else:
		print(f'{num} is not a power of 2.')

if __name__ == '__main__':
	main()
