
def check_prime(number):
	# Check individual integers for prime
	if number == 1:
		return False

	if number == 2 or number == 3:
		return True

	if number % 2 == 0 or number % 3 == 0:
		return False

	# For numbers larger than equal to 5, check for prime
	i = 5
	while i*i <= number:
		if number % i == 0 or number % (i+2) == 0:
			return False
		i += 6

	return True


if __name__ == "__main__":
	# Read integer input from stdin
	T = int(input())

	for _ in range(T):
		# Read input integer from stdin
		n = int(input())

		# Check for prime
		if check_prime(n) == True:
			print("Prime")
		else:
			print("Not prime")
