import math

def main():
	print("Generating e upto n (cannot exceed 15) number of decimal places.")
	N = int(input("Enter n: "))
	e = round(math.e, N)
	print(f"e up to {N} decimal places = {e}")

if __name__ == '__main__':
	main()