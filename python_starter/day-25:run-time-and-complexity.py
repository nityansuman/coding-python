"""
Objective
	Today we're learning about running time!

Task
	A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
	Given a number, n, determine and print whether it's `Prime` or `Not prime`.

Input Format
	The first line contains an integer, T, the number of test cases.
	Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
	1 <= T <= 30
	1 <= n <= 2 x 10^9

Output Format
	For each test case, print whether n is Prime or Not prime on a new line.

Sample Input
	3
	12
	5
	7

Sample Output
	Not prime
	Prime
	Prime
"""


# Method to check if a number is prime or not
def check_prime(number):
	if number == 1:
		return False

	if number == 2 or number == 3:
		return True

	# Any number greater than 3 being divisible by 2 or 3 cannot be prime
	# Prime numbers are only divisible and 1 and itself
	if number % 2 == 0 or number % 3 == 0:
		return False

	# All prime numbers are of form 6K +/- i: for some K and i: 0, 1, 2, 3, 4
	i = 5
	while i*i <= number:
		if number % i == 0 or number % (i+2) == 0:
			return False
		i += 6
	return True


# Entry point of the program
if __name__ == "__main__":
	# Read number of test cases
	T = int(input())

	for _ in range(T):
		# Read number to check prime or not
		n = int(input())
		if check_prime(n) == True:
			print("Prime")
		else:
			print("Not prime")