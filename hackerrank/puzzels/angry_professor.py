def angry_professor(k: int, arr: list) -> str:
	return "NO" if arr[k-1] <= 0 else "YES"


if __name__ == "__main__":
	num_test = int(input().strip())

	for t in range(num_test):
		n, k = map(int, input().strip().split())

		arr = list(map(int, input().rstrip().split()))
		arr = sorted(arr, key=int)

		print("Is class canceled:", angry_professor(k, arr))
