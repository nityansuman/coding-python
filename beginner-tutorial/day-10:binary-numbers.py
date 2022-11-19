"""
Objective
	Today, we're working with binary numbers.

Task
	Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format
	A single integer, n.

Constraints
	1 <= n <= 10e6

Output Format
	Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1
	5

Sample Output 1
	1

Sample Input 2
	13

Sample Output 2
	2
"""


# Convert integer to binary string
def binary(n):
	return bin(n)[2:]

# Sequencial solution to count consecutive 1's in binary representation of an integer
def count_ones(b):
	maxi = 0
	count = 0
	flag = False

	for i in b:
		if i == "1" and flag == False:
			count += 1
			flag = True
		elif i == "1" and flag == True:
			count += 1
		elif i == "0" and flag == True:
			maxi = max(maxi, count)
			count = 0
			flag = False
		else:
			continue
	maxi = max(maxi, count)
	return maxi


if __name__ == "__main__":
	# Read integer input
	n = int(input())

	# Conver the integer to binary format
	binary_rep = binary(n)

	# Count number of consecutive 1's
	max_consecutive_ones = count_ones(binary_rep)

	print(max_consecutive_ones)