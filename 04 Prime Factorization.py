import math

def main():
	print("Generating the prime factors of a given number.")
	num = int(input("\nEnter a number: "))
	
def prime_factors(n): 
	count = 0

	while n % 2 == 0: #Dividing the number as many times as possible by 2.
		print(2)
		n /= 2
		count += 1 

	#Dividing the number by all possible odd numbers (now that the number is no longer an enven number).
	for num in range(3,int(math.sqrt(n)+1), 2): 
		while n % num == 0: #As many times as possible by each number. 
			print(num)
			n /= num
			count += 1

	if count == 0: # In essence, if none of the loops have ever been executed. Will happen only in case of odd primes. 
		print(int(n)) 
prime_factors(num)

if __name__ == '__main__':
	main()
