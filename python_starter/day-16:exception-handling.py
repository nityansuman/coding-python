"""
Objective
	Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message.

Task
	Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
	Note: You must use the String-to-Integer and exception handling constructs built into your submission language.

Input Format
	A single string, S.

Constraints
	1 <= |S| <= 6, where |S| is the length of string .
 	S is composed of either lowercase letters (a-z) or decimal digits (0-9).

Output Format
	Print the parsed integer value of S, or Bad String if S cannot be converted to an integer.

Sample Input 0
	3

Sample Output 0
	3

Sample Input 1
	za

Sample Output 1
	Bad String
"""


if __name__ == "__main__":
	# Read input string
	s = input()

	# Convert string to integer else prompt message
	try:
		s_int = int(s)
	except Exception as e:
		print("Bad String")
	else:
		print(s_int)