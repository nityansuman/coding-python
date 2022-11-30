# Import packages
import re


if __name__ == "__main__":
	N = int(input().strip())

	users = list()

	for N_itr in range(N):
		first_name, email_id = input().rstrip().split()

		# Search using regex
		if re.search("@gmail", email_id):
			users.append(first_name)

	users = sorted(users)
	for user in users:
		print(user)
