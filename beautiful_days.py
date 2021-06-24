"""
Logan wants to go to the movies with Lily on some day x satisfying, i<= x <=j but he knows she only goes to the movies on days she considers to be beautiful. Lily considers a day to be beautiful if the absolute value of the difference between x and reverse(x) is evenly divisible by some k.

Given i, j and k find the number of beautiful days in the inclusive range.
Do not worry about the boundary conditions.

print the count of days as output.
"""

if __name__ == "__main__":
	N, M, K = [int(t) for t in input().strip().split(" ")]
	COUNT = 0

	for x in range(N, M+1):
		y = int(str(x)[::-1])
		if (abs(x - y) % K) == 0:
			COUNT += 1

	print(COUNT)
