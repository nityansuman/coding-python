"""
Objective
	Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops.

Task
	Given a string, s, of length n that is indexed from 0 to n-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format
	The first line contains an integer, T (the number of test cases).
	Each line i of the T subsequent lines contain a String, s.

Constraints
	1 <= T <= 100
	2 <= length of s <= 10000

Output Format
	For each String sj (where 0 <= j <= T-1), print sj's even-indexed characters, followed by a space, followed by sj's odd-indexed characters.

Sample Input
	2
	Hacker
	Rank

Sample Output
	Hce akr
	Rn ak
"""


if __name__ == "__main__":
	# Read number of test cases from stdin
	T = int(input())

	# For each test case
	for i in range(T):
		# Read a string from stdin
		s = input()

		# Initialize two empty strings
		even_string = ""
		odd_string = ""

		# Loop once to create two even and odd indexed strings
		for j in range(len(s)):
			if j%2 == 0:
				even_string += s[j]
			else:
				odd_string += s[j]
		# Print strings with a space in the middle
		# Here creating a format string to do the same
		print(f"{even_string} {odd_string}")