def main():

	print("Generating Fibonacci Sequence up to n number of integers.")
	for item in fibo():
		print(item)
		
def fibo():
	'''
	The Fibonacci series looks like:
	1 1 2 3 5 8...
	It sums up last two predecessors of the series to form the next successor. 
	The series starts from either 0 or 1. 
	'''
	n = int(input("Enter n: "))
	a = 1 #Taking the series to start with a 1 
	b = 1

	for number in range(n):
		yield a
		a,b = b,a+b
			
if __name__ == '__main__':
	main()
