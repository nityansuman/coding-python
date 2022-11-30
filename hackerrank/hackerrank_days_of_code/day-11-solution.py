
if __name__ == "__main__":
	# Array placeholder
	A = list()

	# Read 2D array input from stdin
	for _ in range(6):
		A.append(list(map(int, input().rstrip().split())))

	maxsum = -999

	# Traverse through 2D array and compute sum
	for i in range(4):
		for j in range(4):
			value = A[i][j] + A[i][j+1] + A[i][j+2] + A[i+1][j+1] + A[i+2][j] + A[i+2][j+1] + A[i+2][j+2]
			if value > maxsum:
				maxsum = value
			else:
				continue

	print(maxsum)
