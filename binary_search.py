# Binary Search Implementation

def binary_search(arr, search):
	if len(arr) == 0:
		raise AssertionError("Empty array found!")

	if len(arr) == 1:
		if arr[0] == search:
			return True
		else:
			return False

	mid = len(arr) // 2

	if arr[mid] == search:
		return True

	if search <= arr[mid]:
		return binary_search(arr[:mid], search)
	else:
		return binary_search(arr[mid:], search)


if __name__ == "__main__":
	arr = list(map(int, input().strip().split()))
	search = list(map(int, input().strip().split()))

	for s in search:
		print(f"Searching for {s} in {arr}:", end=" --> ")
		print("Found (?):", binary_search(arr, s))
