"""
Objective
	Today, we're learning about Interfaces.

Task
	Implement Calculator class, which implements the AdvancedArithmetic interface.
	The implementation for the divisor_sum(n) method must return the sum of all divisors of n.

Input Format
	A single line containing an integer, n.

Constraints
	1 <= n <= 1000

Output Format
	Print the sum of the divisor of n.

Sample Input
	6

Sample Output
	12
"""


# Base template class
class AdvancedArithmetic(object):
	# Method template
    def divisor_sum(n):
        raise NotImplementedError


# Main class
class Calculator(AdvancedArithmetic):
	# Class constructor
	def __init__(self):
		pass

	# Method implementation to compute sum of divisors
	def divisor_sum(self, n):
		# Number is always a divisor of itself
		divisor = n
		# Highest divisor of a number other than itself can be n/2
		# No number greater than n/2 can divide n except n itself
		for i in range(1, (n//2)+1):
			if n % i == 0:
				# When no remainder
				divisor += i
			else:
				continue
		return divisor


# Entry point of the program
if __name__ == "__main__":
	# Read input integer
	n = int(input())

	# Initiate class
	my_calculator = Calculator()

	# Compute sum of divisor
	s = my_calculator.divisor_sum(n)

	# Print output
	print(s)