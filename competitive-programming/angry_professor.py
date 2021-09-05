def angry_professor(k: int, arr: list) -> str:
	return "NO" if arr[k-1] <= 0 else "YES"


if __name__ == "__main__":
	# Read number test cases
	num_test = int(input().strip())

	for t in range(num_test):
		# Read students in class (n) and cancelation threshold (k)
		n, k = map(int, input().strip().split())

		# Read n-separated integers describing student arrival times
		arr = list(map(int, input().rstrip().split()))
		arr = sorted(arr, key=int)

		# Determine if class is canceled
		print("Is class canceled:", angry_professor(k, arr))
