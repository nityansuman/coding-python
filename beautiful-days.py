
if __name__ == "__main__":
	# Read input from stdin
	N, M, K = [int(t) for t in input().strip().split(" ")]

	# Set counter
	count = 0

	# Count beautiful days
	for x in range(N, M+1):
		y = int(str(x)[::-1])

		if (abs(x - y) % K) == 0:
			count += 1

	print(count)
