
if __name__ == "__main__":
	# Read integre input from stdin
	n = int(input().strip())

	# Dictionary/mapping placehodler
	teleophone_directory = dict()

	# Read name and number input from stdin
	for i in range(n):
		name, phone_number = input().strip().split()

		# Store as a mapping
		teleophone_directory[name] = phone_number

	# Read an unknown number of query inputs from stdin
	while True:
		search_name = input().strip()
		if not search_name:
			break
		else:
			if search_name in teleophone_directory.keys():
				print(f"{search_name}={teleophone_directory[search_name]}")
			else:
				print("Not found")
