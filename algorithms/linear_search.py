
def linear_search(arr, search):
	for i in range(len(arr)):
		if arr[i] == search:
			return True
	return False


# Test
if __name__ == "__main__":
	# Read an array from stdin
	arr = list(map(int, input().strip().split()))

	# Read search array from stdin
	search = list(map(int, input().strip().split()))

	# Search in the array
	for s in search:
		print(f"Searching for {s} in [{arr}]:", end=" -> ")
		flag = linear_search(arr, s)
		print("Found:", flag)
