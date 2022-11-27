if __name__ == "__main__":
	t = int(input().strip())

	x = 3
	total, diff, n = 0, 0, 0

	while t > total:
		diff = (x * 2**(n+1)) - (x * 2**n)
		total += diff
		n += 1

	print(total - t + 1)
