"""
Given a seqeunce of characters (string) (all same case), find the largest in-order span.

An in-order span is defined as set of characters in ASCII increasing order
with or without gaps i.e., `abf` is in-order but `fb` is not in-order.

Note:
- In case of multiple string spans with same length print the first one.
- Input sequence can have repeatition of characters.

Example:
	abcde -> abcde
	dabc -> abc
	cdeah -> cde
	ababdf -> abdf
"""


def largest_inorder_span(string):
	# Set variables
	prev_char = None
	span_index, global_span_index = list(), list()

	for c in string:
		# Get character index
		index = string.index(c)

		if prev_char is None:
			# Set first character index
			span_index.append(index)
		else:
			if c > prev_char:
				# Add character index
				span_index.append(index)
			else:
				if len(span_index) > len(global_span_index):
					# Update global span index
					global_span_index = span_index
					# Reset span index
					span_index = [index]

		# Set current character to previous for lookup
		prev_char = c

	# Update global span index for edge caase handling
	if len(span_index) > len(global_span_index):
		global_span_index = span_index

	# Construct in-order string
	return "".join([string[i] for i in global_span_index])


if __name__ == "__main__":
	# Read integer input denoting number of tests cases from stdin
	tests = int(input().strip())

	for t in range(tests):
		# Read string input from stdin
		string = input().strip()

		# Get largest in-order span
		print(largest_inorder_span(string))
