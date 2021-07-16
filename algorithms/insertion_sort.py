
def insertion_sort(arr):
	# Raise error if array is empty
	if len(arr) == 0:
		raise AssertionError("Empty array found.")

	# Return array if only one element found
	if len(arr) == 1:
		return arr

	# Iterate over the array
	for i in range(1, len(arr)):
		# Set first key at index 1
		key = arr[i]

		# Iterate backwards and create space
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1

		# Add key at appropriate place
		arr[j+1] = key

	return arr


# Test
if __name__ == "__main__":
	# Read input array from stdin
	arr = list(map(int, input().strip().split()))

	# Compute method to perform insertion sort
	sorted_arr = insertion_sort(arr)

	# View sorted array
	print("Sorted array:", sorted_arr)
