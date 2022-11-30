
class Calculator:
	def power(self, n, p):
		# Compute `n` to the power of `p`
		if n >= 0 and p >= 0:
			return n**p
		else:
			raise Exception("n and p should be non-negative")


if __name__ == "__main__":
	# Initiate the above class
	myCalculator = Calculator()

	# Read test case integer input from stdin
	T = int(input().strip())

	# Iterate over number of test cases
	for i in range(T):
		# Read integer input from stdin
		n, p = map(int, input().split())

		# Use exception handling
		try:
			# Compute result
			ans = myCalculator.power(n,p)
		except Exception as e:
			# Handle and print exception
			print(e)
		else:
			# Print result if everything goes fine
			print(ans)
