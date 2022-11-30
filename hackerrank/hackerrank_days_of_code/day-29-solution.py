
if __name__ == "__main__":
	# Read integer input from stdin
	t = int(input())

	for t_itr in range(t):
		# Read string input from stdin
		n, k = list(map(int, input().split()))
		# Compute bitwise and max value
		print(k-1 if ((k-1) | k) <= n else k-2)
