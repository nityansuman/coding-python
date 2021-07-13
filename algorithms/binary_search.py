
def binary_search(arr, search):
	# Check for empty array
	if len(arr) == 0:
		raise AssertionError("Empty array found!")

	# Check for single element in array
	if len(arr) == 1:
		if arr[0] == search:
			return True
		else:
			return False

	# Compute middle index
	if len(arr) % 2 == 0:
		mid = len(arr) // 2
	else:
		mid = len(arr) // 2

	# Check in middle index
	if arr[mid] == search:
		return True

	# Recursive call to either side of the array
	if search <= arr[mid]:
		return binary_search(arr[0:mid], search)
	else:
		return binary_search(arr[mid:], search)


# Test
if __name__ == "__main__":
	# Read sorted array from stdin
	arr = list(map(int, input().strip().split()))

	# Read search array from stdin
	search = list(map(int, input().strip().split()))

	# Search in the array
	for s in search:
		print(f"Searching for {s} in [{arr}]:", end=" -> ")
		flag = binary_search(arr, s)
		print("Found:", flag)
