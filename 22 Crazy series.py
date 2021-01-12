'''
Problem statement:
0, 0, 2, 1, 4, 2, 6, 3, 8...
In the above series, values at every odd position is an even number in ascending 
order and at every even position is the value of the previous position divided 
by 2. Print the series till the nth position and give the value present at the 
mth position.
'''

value_at = {1: 0, 2: 0, 3: 2, 4: 1} #Initializing a dictionary with the keys as 
									#positiona and value as the corresponding 
									#number of the series.

def output(n, m):
	if n not in value_at.keys(): #In case our dictionary hasn't been initialized
								 #till n...
		for i in range(n, 4, -1): #We get the last position till which it has 
			if i in value_at.keys(): #been initialized.
				break
		for j in range(i, n+1): #And update our dictionary from that position 
								#till the nth position
			if j % 2 == 0:	#If the position j is even...	
				value_at[j] = j // 2 - 1 #We give it a value of (j/2)-1.
			else:
				value_at[j] = j - 1 #Else, we give it a value of j-1.
				
	print(f"The series till {n}th position is:")
	for i in range(1, n+1): #Finally we print the series.
		print(f"{value_at[i]},", end = "") 
	if m in value_at.keys():
		print(f"{value_at[m]}")
	else: 
		value_at_m = (m // 2 - 1) if m % 2 == 0 else m - 1
		print(f"\nValue at {m}: {value_at_m}")


def main():
	output(10, 555)

if __name__ == '__main__':
	main()


