fibo_cache = {}

def fibo(n):
	'''
	Returns the fibonacci sequence upto n terms. 
	'''

	if n in fibo_cache:
		return fibo_cache[n]

	if n == 0 or n == 1 or n == 2:
		value = 1
	else:
		value = fibo(n-1) + fibo(n-2)
	
	fibo_cache[n] = value
	return value

def main():
	for i in range(1,10001):
		print(fibo(i))

if __name__ == '__main__':
	main()

