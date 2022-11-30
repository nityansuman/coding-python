def utopian_tree(n):
	height = 1
	is_summer = True

	if n == 0:
		return height

	while n > 0:
		if is_summer:
			height *= 2
			is_summer = False
			n -= 1
		if not is_summer and n > 0:
			height += 1
			is_summer = True
			n -= 1

	return height


if __name__ == "__main__":
	t = int(input().strip())

	for x in range(t):
		n = int(input().strip())
		print("Height of the `Utopian` tree:", utopian_tree(n))
