
def bubble_sort(array):
	num_swaps = 0
	for i, _ in enumerate(array):
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				# Swap
				array[i], array[j] = array[j], array[i]
				num_swaps += 1
			else:
				continue
	return num_swaps, array


if __name__ == "__main__":
	# Read input integre from stdin
	N = int(input().strip())

	# Read array input from stdin
	A = list(map(int, input().strip().split()))

	# Perform bubble sort on array
	num_swaps, A = bubble_sort(A)

	print(f"Array is sorted in {num_swaps} swaps.")
	print(f"First Element: {A[0]}")
	print(f"Last Element: {A[-1]}")
