if __name__ == "__main__":
	rows, columns = list(map(int, input().strip().split()))

	data = list()
	for i in range(rows):
		data.append(list(map(int, input().strip().split())))

	sort_col_index = int(input().strip())

	for row in sorted(data, key=lambda t: t[sort_col_index]):
		print(" ".join([str(x) for x in row]).strip())
