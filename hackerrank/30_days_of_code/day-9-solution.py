
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)


if __name__ == "__main__":
	# Read file path from stdin
	OUTPUT_PATH = input().strip()

	# Open a file in write mode
	fptr = open(OUTPUT_PATH, "w")

	# Read integer input from stdin
	n = int(input().strip())

	# Compute factorial result and save to a variable
	result = factorial(n)

	# Write result to the output file
	# Add a newline
	fptr.write(str(result) + "\n")

	# Close output file
	fptr.close()
