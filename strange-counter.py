
if __name__ == "__main__":
	# Read input from stdin
	T = int(input().strip())

	# Set counter start
	X = 3

	# Placeholder variables
	total, diff, n = 0, 0, 0

	# Compute final counter value
	while T > total:
		diff = (X * 2**(n+1)) - (X * 2**n)
		total += diff
		n += 1

	print(total - T + 1)
