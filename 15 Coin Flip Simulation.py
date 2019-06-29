from random import *

def main():

	print("This program simulates a coin flip.")
	sim_num = int(input("\nHow many times do you wish to flip a coin?\n\t"))
	record = {'Heads': 0, 'Tail': 0}

	for instance in range (sim_num):
		if randint(0,1) == 0:   #Let 0 represent a tail.
			record['Tail'] += 1
		else: 					#Let 1 represent a heads.
			record['Heads'] += 1

	print(f"\nTotal:\n\tHeads = {record['Heads']}\n\tTails = {record['Tail']}")

if __name__ == '__main__':
	main()