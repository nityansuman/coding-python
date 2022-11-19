"""Linear Search Implementation"""

def linear_search(arr, search):
	for _, ele in enumerate(arr):
		if ele == search:
			return True

	return False


if __name__ == "__main__":
	arr = list(map(int, input().strip().split()))
	search = list(map(int, input().strip().split()))

	for s in search:
		print(f"Searching for {s} in [{arr}]:", end=" --> ")
		print("Found (?):", linear_search(arr, s))
