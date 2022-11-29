"""
Objective
	Today, we're learning about the Array data structure.

Task
	Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format
	The first line contains an integer, N (the size of our array).
	The second line contains N space-separated integers describing array A's elements.

Constraints
	1 <= N <= 100
	1 <= Ai <= 10000, where Ai is the ith integer in the array.

Output Format
	Print the elements of array  in reverse order as a single line of space-separated numbers.

Sample Input
	4
	1 4 3 2

Sample Output
	2 3 4 1
"""


if __name__ == "__main__":
	# Read size of array from stdin
	N = int(input())

	# Create array output of stdin
	# Strip spaces from input and split on spaces and then convert string character to integer
	A = [int(i) for i in input().strip().split()]

	# Use while loop to reverse access array elements
	i = N-1
	while i >= 0:
		# Print element with space as end character rather than newline character
		print(A[i], end=" ")
		i -= 1