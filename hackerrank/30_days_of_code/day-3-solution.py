
def if_weird(value):
	if value % 2 != 0:
		# Odd number
		return "Weird"
	else:
		# Even number
		if value in range(2, 5+1):
			return "Not Weird"
		elif value in range(6, 20+1):
			return "Weird"
		elif value > 20:
			return "Not Weird"


if __name__ == "__main__":
	# Read an integer number from stdin (standard input)
	N = int(input().strip())

	# Get results using a method
	print(if_weird(N))
