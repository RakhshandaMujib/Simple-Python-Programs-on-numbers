import timeit

fibo_cache = {0: 1, 1: 1, 2: 1}

def fibo_dynamic(n):
	'''
	Makes use of the fibo_cache dictionary to retrieve the nth value 
	of the sequence. If the nth value is not present, it adds it to the
	dictionary for the (n+1)th value.
	'''
	if n in fibo_cache.keys():
		return fibo_cache[n]

	fibo_cache[n] = fibo_dynamic(n-1) + fibo_dynamic(n-2)

	return fibo_cache[n]

def dynamic_time(): 
    SETUP_CODE = '''
from __main__ import fibo_dynamic'''
  
    TEST_CODE = ''' 
value = 0
for i in range(1, 101): #Change the range if you want.
	value = fibo_dynamic(i)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('Fibonacci using dynamic programming: {}'.format(min(times))) 

def fibo_generator():
	'''
	Simply yields the nth value of in the sequence. 
	'''
	a = 1  
	b = 1

	for number in range(100): #Change the range if you want.
		yield a
		a,b = b,a+b

def generator_time(): 
    SETUP_CODE = '''
from __main__ import fibo_generator 
from random import randint'''
  
    TEST_CODE = ''' 
value = 0
for i in fibo_generator():
	value = i'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('Fibonacci using generator: {}'.format(min(times))) 


if __name__ == "__main__":  
    dynamic_time()
    generator_time()