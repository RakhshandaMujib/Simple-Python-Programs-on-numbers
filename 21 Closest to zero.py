'''
Problem statement:
Given any input arrray A find the number that is closest to 0.
'''
A = [5, 4, -1, -2, 6, 100]
closeset = A[0]
for i in range(1, len(A)):
	closeset = closeset if closeset < abs(A[i]) else A[i]
print(closeset)