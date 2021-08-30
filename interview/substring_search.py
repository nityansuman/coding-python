"""
Given a string and a pattern, write a program to find if the pattern is present in the string.

Example:
	string = "HelloWorld"
	pattern = "World"
	output = True

	string = "Hellohello"
	pattern = "hello"
	output = True

	string = "Hellohello"
	pattern = "helo"
	output = False
"""


def exact_match(string, pattern, s_index, p_index):
	# Check if we have reached end of pattern
	if p_index == len(pattern):
		return True

	# Check if we have reached end of string and still match is pending
	if s_index == len(string):
		return False

	if string[s_index] == pattern[p_index]:
		# If current index matches, go to next
		return exact_match(string, pattern, s_index+1, p_index+1)

	# If no match found, return False
	return False


def substring_search(string, pattern, s_index, p_index):
	# Check base input
	if len(string) < len(pattern):
		raise AssertionError("Search string greater than the main string.")

	# Check if we have gone too far
	if s_index > len(string):
		return False

	if exact_match(string, pattern, s_index, p_index):
		# If found return True
		return True

	# Search from next position
	return substring_search(string, pattern, s_index+1, p_index)


# Test
if __name__ == "__main__":
	# Read a string from stdin
	string = input().strip()

	# Read search string from stdin
	pattern = input().strip()

	flag = substring_search(string, pattern, 0, 0)
	print(f"Finding pattern = `{pattern}` in `{string}`: {flag}")
