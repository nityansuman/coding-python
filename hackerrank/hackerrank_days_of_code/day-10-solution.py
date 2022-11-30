
def count_ones(binary_number):
	max_count, count = 0, 0
	flag = False

	for b in binary_number:
		if b == "1":
			if flag == False:
				# Start counting
				count += 1
				flag = True
			elif flag == True:
				# Keep counting
				count += 1
		elif b == "0":
			if flag == True:
				# Stop counting
				max_count = max(max_count, count)

				# Reset
				count = 0
				flag = False
			elif flag == False:
				# Do nothing
				continue
	# In case last binary literal is 1
	# Counting never stopped
	max_count = max(max_count, count)
	return max_count


if __name__ == "__main__":
	# Read integer input from stdin
	n = int(input().strip())

	# Conver input integer to binary
	# Remove binary literals "0b"
	binary_rep = bin(n)[2:]

	# Count consecutive 1s
	max_consecutive_ones = count_ones(binary_rep)

	print(max_consecutive_ones)
