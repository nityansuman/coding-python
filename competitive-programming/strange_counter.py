if __name__ == "__main__":
	# Read number of test cases input from stdin
	t = int(input().strip())

	x = 3 # Counter start

	# Placeholder variables
	total, diff, n = 0, 0, 0

	# Compute counter
	while t > total:
		diff = (x * 2**(n+1)) - (x * 2**n)
		total += diff
		n += 1

	print(total - t + 1)
