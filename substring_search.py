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
	if p_index == len(pattern):
		return True

	if s_index == len(string):
		return False

	if string[s_index] == pattern[p_index]:
		return exact_match(string, pattern, s_index+1, p_index+1)

	return False

def substring_search(string, pattern, s_index, p_index):
	if len(string) < len(pattern):
		raise AssertionError("Search string greater than the main string.")

	if s_index > len(string):
		return False

	if exact_match(string, pattern, s_index, p_index):
		return True

	return substring_search(string, pattern, s_index+1, p_index)


if __name__ == "__main__":
	string = input().strip()
	pattern = input().strip()

	flag = substring_search(string, pattern, 0, 0)

	print(f"Finding pattern = `{pattern}` in `{string}`: {flag}")
