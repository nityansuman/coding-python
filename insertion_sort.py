# Insertion Sort Implementation

def insertion_sort(arr, ascending=True):
	if len(arr) == 0:
		raise AssertionError("Empty array found.")

	if len(arr) == 1:
		return arr

	for i in range(1, len(arr)):
		key = arr[i]

		j = i-1

		if ascending:
			while j >= 0 and key < arr[j]:
				arr[j+1] = arr[j]
				j -= 1
		else:
			while j >= 0 and key > arr[j]:
				arr[j+1] = arr[j]
				j -= 1

		arr[j+1] = key

	return arr


if __name__ == "__main__":
	arr = list(map(int, input().strip().split()))
	print("Input array:", arr)
	print("Sorted array:",  insertion_sort(arr, ascending=True))
