if __name__ == "__main__":
	# Read input from stdin
	n, m = input().strip().split(" ")
	n, m = [int(n), int(m)]

	# Draw top half
	for i in range(1, n, 2):
		print("-" * ((m - i * 3) // 2) + ("|".center(3, "."))
				  * i + "-" * ((m - i * 3) // 2))

	# Print message
	print("WELCOmE".center(m, "-"))

	# Draw bottom half
	for i in range(n - 2, -1, -2):
		print("-" * ((m - i * 3) // 2) + ("|".center(3, "."))
				  * i + "-" * ((m - i * 3) // 2))
