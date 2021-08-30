"""
Give two sorted arrays a1 and a2, write a program to merge into a single array in same order.

If the arrays (a1 and a2) are in ascending order, then merged array should also be in
ascending order and vice-versa.

Example:
	a1 = [1, 3, 5, 7, 9]
	a2 = [2, 4, 6, 8]
	order = True # Ascending order
	Merged array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	a1 = [5, 3, 1]
	a2 = [6, 4, 2]
	order = False # Descending order
	Merged array = [6, 5, 4, 3, 2, 1]
"""


def join_sorted_arrays(arr1, arr2, asc):
	# Compute length of arrays
	len1, len2 = len(arr1), len(arr2)

	# Placeholder for the merged arrays
	arr = list()

	# Set starting indexes
	idx1, idx2 = 0, 0

	# Iterate over arrays untill one of them runs over
	while idx1 < len1 and idx2 < len2:
		if asc is True:
			# Ascending order
			if arr1[idx1] < arr2[idx2]:
				arr.append(arr1[idx1])
				idx1 += 1
			elif arr1[idx1] > arr2[idx2]:
				arr.append(arr2[idx2])
				idx2 += 1
			else:
				arr.extend((arr1[idx1], arr2[idx2]))
				idx1 += 1
				idx2 += 1
		else:
			# Descending order
			if arr1[idx1] > arr2[idx2]:
				arr.append(arr1[idx1])
				idx1 += 1
			elif arr1[idx1] < arr2[idx2]:
				arr.append(arr2[idx2])
				idx2 += 1
			else:
				arr.extend((arr1[idx1], arr2[idx2]))
				idx1 += 1
				idx2 += 1

	# Append rest of the array
	if idx1 < len1:
		arr.extend(arr1[idx1:])
	else:
		# That means, idx2 < len2
		arr.extend(arr2[idx2:])

	return arr


# Test
if __name__ == "__main__":
	# Read integer arrays from stdin
	a1 = list(map(int, input().strip().split()))
	a2 = list(map(int, input().strip().split()))

	# Read ascending order flag
	# If True, sorted in ascending order else descending order
	# Options: `True`, `False`
	order = eval(input().strip())

	# Call method to merge arrays in same sorted order
	merged_arr = join_sorted_arrays(a1, a2, asc=order)
	print("Merged array:", merged_arr)
