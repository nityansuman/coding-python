def piling_up(num_blocks: int, block_lengths: int) -> bool:
	top = -1
	left, right = 0,
	num_blocks - 1

	if_first, flag = True, True

	while left < right:
		if block_lengths[left] > block_lengths[right]:
			if if_first:
				top = block_lengths[left]
				left += 1

				if_first = False
			else:
				if block_lengths[left] <= top:
					top = block_lengths[left]
					left += 1
				else:
					flag = False
					break
		elif block_lengths[left] < block_lengths[right]:
			if if_first:
				top = block_lengths[right]
				right -= 1

				if_first = False
			else:
				if block_lengths[right] <= top:
					top = block_lengths[right]
					left += 1
				else:
					flag = False
					break
		else:
			if if_first:
				top = block_lengths[left]
				left += 1
				right -= 1

				if_first = False
			else:
				if block_lengths[left] <= top:
					top = block_lengths[left]
					left += 1
					right -= 1
				else:
					flag = False
					break
	return flag


if __name__ == "__main__":
	test_cases = int(input().strip())

	for t in range(test_cases):
		num_blocks = int(input().strip())

		block_lengths = list(map(int, input().strip().split()))
		flag = piling_up(num_blocks, block_lengths)

		if flag:
			print("Yes")
		else:
			print("No")
