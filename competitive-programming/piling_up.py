
def piling_up(num_blocks, block_lengths):
	# Set dummy top value
	top = -1

	# Set left and right pointers
	left, right = 0, num_blocks - 1

	# Set flag to denote first iteration
	if_first = True

	# Set flag to indicate if piling is possible
	flag  = True

	# Iterate over the block lengths using two pointers
	while left < right:
		# Find the largest block length
		if block_lengths[left] > block_lengths[right]:
			if if_first:
				# First iteration
				top = block_lengths[left]
				left += 1

				# Reset flag to avoid running this block for other iterations
				if_first = False
			else:
				if block_lengths[left] <= top:
					top = block_lengths[left]
					left += 1
				else:
					# Reset piling up flag when rule failes and break
					flag = False
					break
		elif block_lengths[left] < block_lengths[right]:
			if if_first:
				# First iteration
				top = block_lengths[right]
				right -= 1

				# Reset flag to avoid running this block for other iterations
				if_first = False
			else:
				if block_lengths[right] <= top:
					top = block_lengths[right]
					left += 1
				else:
					# Reset piling up flag when rule failes and break
					flag = False
					break
		else:
			if if_first:
				# First iteration
				top = block_lengths[left]
				left += 1
				right -= 1

				# Reset flag to avoid running this block for other iterations
				if_first = False
			else:
				if block_lengths[left] <= top:
					top = block_lengths[left]
					left += 1
					right -= 1
				else:
					# Reset piling up flag when rule failes and break
					flag = False
					break
	return flag


if __name__ == "__main__":
	# Read number test cases from stdin
	test_cases = int(input().strip())

	# For each test case
	for t in range(test_cases):
		# Read number of blocks from stdin
		num_blocks = int(input().strip())

		# Read block side lengths from stdin
		block_lengths = list(map(int, input().strip().split()))

		# Check for piling
		flag = piling_up(num_blocks, block_lengths)

		# Print appropriate message
		if flag:
			print("Yes")
		else:
			print("No")
