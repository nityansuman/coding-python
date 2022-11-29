"""
Objective
	Today's challenge puts your understanding of nested conditional statements to the test.

Task
	Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

	1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)
	2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 hackos * (the number of days late).
	3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, then ine = 500 hackos * (the number of months late).
	4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.

Input Format
	The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned.
	The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Constraints
	1 <= D <= 31
	1 <= M <= 12
	1 <= Y <= 3000
	It is also guaranteed that the date will be avalid calendar date.

Output Format
	Print a single integer denoting the library fine for the book received as input.

Sample Input
	9 6 2015
	6 6 2015

Sample Output
45
"""


def compute_fine(actual_date, expected_date):
	# Method to compute library fine
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


# Entry point of the program
if __name__ == "__main__":
	# Read first date
	actual_date = list(map(int, input().strip().split()))

	# Read second date
	expected_date = list(map(int, input().strip().split()))

	fine = compute_fine(actual_date, expected_date)
	print(fine)