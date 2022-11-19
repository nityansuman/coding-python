"""
Objective
	Today, we're learning and practicing an algorithmic concept called Recursion.

Task
	Write a factorial function that takes a positive integer, n as a parameter and prints the result of n! (n factorial).

Note: You must use recursion to compute factorial.

Input Format
	A single integer, n (the argument to pass to factorial).

Constraints
	2 <= n <= 12
	Your submission must contain a recursive function named factorial.

Output Format
	Print a single integer denoting n!.

Sample Input
	3

Sample Output
	6
"""


# Recursive method to compute factorial of a number
def factorial(a):
	if a == 0 or a == 1:
		return 1
	else:
		return a * factorial(a-1)


if __name__ == "__main__":
	# Read integer input
	n = int(input())

	# Compute factorial of the number
	result = factorial(n)

	print(result)