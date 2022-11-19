"""
Objective
	In this challenge, we review some basic concepts that will get you started with this series. You will need to use the same (or similar) syntax to read input and write output in challenges throughout HackerRank.

Task
	To complete this challenge, you must save a line of input from stdin to a variable, print Hello, World. on a single line, and finally print the value of your variable on a second line.

	You've got this!

Note: The instructions are Java-based, but we support submissions in many popular languages. You can switch languages using the drop-down menu above your editor, and the 
`input_string` variable may be written differently depending on the best-practice conventions of your submission language.

Input Format
	A single line of text denoting `input_string` (the variable whose contents must be printed).

Output Format
	Print Hello, World. on the first line, and the contents of `input_string`  on the second line.

Sample Input
	Welcome to 30 Days of Code!

Sample Output
	Hello, World. 
	Welcome to 30 Days of Code!
"""


# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
# Print the input string on a new line.
print(input_string)