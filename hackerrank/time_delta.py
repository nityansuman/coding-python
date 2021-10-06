# Import packages
from datetime import datetime


def time_delta(t1, t2):
	# Compute absolute difference in seconds
	return int(abs((t1 - t2).total_seconds()))


if __name__ == "__main__":
	# Read test cases from stdin
	t = int(input().strip())

	for i in range(t):
		# Read two timestamps with time zone from stdin
		t1 = datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z")
		t2 = datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z")

		# Compute delta in seconds
		delta = time_delta(t1, t2)
		print("Time Delta (seconds):", delta)
