"""
Objective
	Today, we're building on our knowledge of Arrays by adding another dimension.

Context
	Given a 6x6 2D Array, A:

	1 1 1 0 0 0
	0 1 0 0 0 0
	1 1 1 0 0 0
	0 0 0 0 0 0
	0 0 0 0 0 0
	0 0 0 0 0 0

	We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
	a b c
	  d
	e f g

	There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
	Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Input Format
	There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to +9.

Constraints
	-9 <= A[i][j] <= 9
	0 <= i,j <= 5

Output Format
	Print the largest (maximum) hourglass sum found in A.

Sample Input
	1 1 1 0 0 0
	0 1 0 0 0 0
	1 1 1 0 0 0
	0 0 2 4 4 0
	0 0 0 2 0 0
	0 0 1 2 4 0

Sample Output
	19
"""


if __name__ == "__main__":
	# Value placeholder
	A = list()

	# Read input
	for _ in range(6):
		A.append(list(map(int, input().rstrip().split())))

	maxsum = -100 # Check constraints: min sum can be -63 and max sum can be 63

	# Traverse through 2D array (nested list in Python) and compute sum for all hourglass pattern to find maximum
	for i in range(4):
		for j in range(4):
			# Python doesn't have array concept and external packages were not allowed
			# Treating nested list as 2D array
			# Nested list do not support 2D slicing, so accessing individual elements
			value = A[i][j] + A[i][j+1] + A[i][j+2] + A[i+1][j+1] + A[i+2][j] + A[i+2][j+1] + A[i+2][j+2]
			if value > maxsum:
				# Updated with a bigger hourglass value
				maxsum = value
			else:
				continue
	print(maxsum)



# # Use external package to get array support for python
# # Import packages
# import numpy as np


# if __name__ == "__main__":
# 	# Value placeholder
# 	A = list()

# 	# Read input
# 	for _ in range(6):
# 		A.append(list(map(int, input().rstrip().split())))

# 	# Convert nested list to an array
# 	A = np.array(A)

# 	maxsum = -100 # Check constraints: min sum can be -63 and max sum can be 63

# 	# Traverse through 2D array and compute sum for all hourglass pattern
# 	for i in range(4):
# 		for j in range(4):
# 			value = np.sum(A[i:i+3, j:j+3]) - (A[i+1, j] + A[i+1, j+2])
# 			if value > maxsum:
# 				# Updated with a bigger hourglass value
# 				maxsum = value
# 			else:
# 				continue
# 	print(maxsum)