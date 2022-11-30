
def compute_fine(actual_date, expected_date):
	fine = 0
	if actual_date[2] <= expected_date[2] and actual_date[1] <= expected_date[1] and actual_date[0] <= expected_date[0]:
		# Actual date is on or before expected date
		fine = 0
	elif actual_date[0] > expected_date[0] and actual_date[1] == expected_date[1] and actual_date[2] == expected_date[2]:
		fine = 15 * (actual_date[0] - expected_date[0])
	elif actual_date[1] > expected_date[1] and actual_date[2] == expected_date[2]:
		fine = 500 * (actual_date[1] - expected_date[1])
	elif actual_date[2] > expected_date[2]:
		fine = 10000
	return fine


if __name__ == "__main__":
	# Read date in list format from stdin
	actual_date = list(map(int, input().strip().split()))

	# Read another date in list format from stdin
	expected_date = list(map(int, input().strip().split()))

	# Compute fine
	print("Fine = ", compute_fine(actual_date, expected_date))
