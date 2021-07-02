
def utopian_tree(n):
	# Set initial height of the tree
	# Set counter
	height, counter = 1, 0

	if n == 0:
		return height

	while n > 0:
		if counter == 0:
			# Update height
			height = 2 * height

			# Set environment
			counter += 1
			n -= 1
		if counter == 1 and n > 0:
			# Update height
			height += 1

			# Set environment
			counter = 0
			n -= 1

	# At the end of the cycle return update height
	return height


if __name__ == "__main__":
	# Read integer input denoting test cases from stdin
	t = int(input().strip())

	# For each test case
	for x in range(t):

		# Read integer input denoting cycles from stdin
		n = int(input().strip())

		# Compute uotpian tree height after n cycles
		height = utopian_tree(n)

		print(height)
