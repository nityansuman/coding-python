
if __name__ == "__main__":
	# Read integer input from stdin
	n = int(input().strip())

	# Read array/list of integer input from stdin
	arr = list(map(int, input().rstrip().split()))

	# Print elements in reverse order
	i = n-1
	while i >= 0:
		print(arr[i], end=" ")
		i -= 1
