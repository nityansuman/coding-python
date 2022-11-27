# https://leetcode.com/problems/valid-parentheses/

class Solution:
	def isValid(self, s: str) -> bool:
		stack = list()

		mapping = {
			"(": ")",
			"{": "}",
			"[": "]",
		}

		for c in s:
			if c in mapping:
				stack.append(mapping[c])
			else:
				if stack:
					if c != stack[-1]:
						return False
					else:
						stack.pop()
				else:
					return False

		return not stack
