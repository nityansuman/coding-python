"""
Objective
	In today's challenge, you're going to practice throwing and propagating an exception.

Task
	Write a Calculator class with a single method: int power(int,int).
	The power method takes two integers, N and P, as parameters and returns the integer result of `n` to the power of `p`.
	If either n or p is negative, then the method must throw an exception with the message: `n and p should be non-negative`.
	Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.

Input Format
	The first line contains an integer, T, the number of test cases.
	Each of the T subsequent lines describes a test case in 2 space-separated integers denoting n and p, respectively.

Output Format
	There are T lines of output, where each line contains the result of n**p (n to the power of p) as calculated by your Calculator class' power method.

Sample Input
	4
	3 5
	2 4
	-1 -2
	-1 3

Sample Output
	243
	16
	n and p should be non-negative
	n and p should be non-negative
"""


# Base class
class Calculator:
	# Class constructor
	def __init__(self):
		pass

	# Method to compute power
	def power(self, n, p):
		if n >= 0 and p >= 0:
			return n**p
		else:
			# Raise / throw exception
			raise Exception("n and p should be non-negative")


# Entry point of the program
if __name__ == "__main__":
	# Initiate class
	myCalculator = Calculator()

	# Read input integer - number of test cases
	T = int(input())

	# For each test case read n and p
	for i in range(T):
		n, p = map(int, input().split())
		# Compute power and print answer
		try:
			# Try to execute
			ans = myCalculator.power(n,p)
			# If no exception is thrown
			print(ans)
		except Exception as e:
			# Catch thrown exception if any and print
			print(e)