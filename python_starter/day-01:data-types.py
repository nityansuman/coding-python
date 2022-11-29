"""
Objective
	Today, we're discussing data types.

Task
	Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:
		1. Declare 3 variables: one of type int, one of type double, and one of type String.
		2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
		3. Use the + operator to perform the following operations:
			Print the sum of i plus your int variable on a new line.
			Print the sum of d plus your double variable to a scale of one decimal place on a new line.
			Concatenate s with the string you read as input and print the result on a new line.

Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

Input Format
	The first line contains an integer that you must sum with i.
	The second line contains a double that you must sum with d.
	The third line contains a string that you must concatenate with s.

Output Format
	Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, and then the two concatenated strings on the third line.

Sample Input
	12
	4.0
	is the best place to learn and practice coding!

Sample Output
	16
	8.0
	HackerRank is the best place to learn and practice coding!
"""


i = 4 # int
d = 4.0 # double
s = 'HackerRank ' # string

input_i = int(input()) # read input string and convert to int
input_d = float(input()) # read input string and convert to floating point
input_s = input() # read string input

# Output
print(i + input_i)
print(d + input_d)
print(s + input_s)