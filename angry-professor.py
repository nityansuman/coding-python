# Import packages
import os

#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
	a = sorted(a, key=int)
	return "NO" if a[k-1] <= 0 else "YES"


if __name__ == "__main__":
	# Open file to write output
	fptr = open(os.environ["OUTPUT_PATH"], "w")

	# Read test cases input from stdin
	t = int(input().strip())

	for t_itr in range(t):
		# Read input from stdin
		first_multiple_input = input().rstrip().split()

		# Process read input
		n = int(first_multiple_input[0])
		k = int(first_multiple_input[1])
		a = list(map(int, input().rstrip().split()))

		# Execute method to get results
		result = angryProfessor(k, a)

		# Write output to file
		fptr.write(result + "\n")

	# Close file
	fptr.close()
