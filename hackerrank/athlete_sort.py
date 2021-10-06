if __name__ == "__main__":
	# Read number of rows and columns from stdin
	rows, columns = list(map(int, input().strip().split()))

	# Read data points from stdin
	data = list()
	for i in range(rows):
		data.append(list(map(int, input().strip().split())))

	# Read sprting index from stdin
	sort_col_index = int(input().strip())

	# Sort data using a particular column index
	for row in sorted(data, key=lambda t: t[sort_col_index]):
		print(" ".join([str(x) for x in row]).strip())
