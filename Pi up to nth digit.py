import math

def main():
	print("Generating pi upto n (cannot exceed 15) number of decimal places.")
	N = int(input("Enter n: "))
	pi = round(math.pi, N)
	print(f"Pi up to {N} decimal places = {pi}")

if __name__ == '__main__':
	main()