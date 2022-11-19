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
	prev_char = None
	span_index, global_span_index = list(), list()

	for c in string:
		index = string.index(c)

		if prev_char is None:
			span_index.append(index)
		else:
			if c > prev_char:
				span_index.append(index)
			else:
				if len(span_index) > len(global_span_index):
					global_span_index = span_index
					span_index = [index]

		prev_char = c

	if len(span_index) > len(global_span_index):
		global_span_index = span_index

	return "".join([string[i] for i in global_span_index])


if __name__ == "__main__":
	tests = int(input().strip())

	for t in range(tests):
		string = input().strip()
		print(largest_inorder_span(string))
