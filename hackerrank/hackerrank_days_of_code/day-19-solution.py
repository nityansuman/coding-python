
class AdvancedArithmetic(object):
	# Base `AdvancedArithmetic` class

	def divisor_sum(n):
		# Method to compute divisor sum
		raise NotImplementedError


class Calculator(AdvancedArithmetic):
	# `Calculator` class inherits `AdvancedArithmetic` class and overrides method

	def divisor_sum(self, n):
		# Method to compute divisor sum
		divisor = n
		for i in range(1, (n//2)+1):
			if n % i == 0:
				divisor += i
			else:
				continue
		return divisor


if __name__ == "__main__":
	# Read integer input from stdin
	n = int(input())

	# Initiate a `Calculator` class
	my_calculator = Calculator()

	# Compute sum of divisor
	s = my_calculator.divisor_sum(n)
	print(s)

	# Print class info
	print("I implemented: " + str(type(my_calculator)))
	print("I implemented: " + type(my_calculator).__bases__[0].__name__)
