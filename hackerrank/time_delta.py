# Import packages
from datetime import datetime

def time_delta(t1, t2):
	return int(abs((t1 - t2).total_seconds()))


if __name__ == "__main__":
	t = int(input().strip())

	for i in range(t):
		t1 = datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z")
		t2 = datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z")
		delta = time_delta(t1, t2)
		print("Time Delta (seconds):", delta)
