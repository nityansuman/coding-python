"""Linear Search Implementation"""

def linear_search(arr, search):
	# Iterate over the array
	for _, ele in enumerate(arr):
		# Check for search element
		if ele == search:
			return True

	return False


if __name__ == "__main__":
	# Read input array from stdin
	arr = list(map(int, input().strip().split()))

	# Read search elements from stdin
	search = list(map(int, input().strip().split()))

	# Search in the array
	for s in search:
		print(f"Searching for {s} in [{arr}]:", end=" -> ")
		flag = linear_search(arr, s)
		print("Found:", flag)
