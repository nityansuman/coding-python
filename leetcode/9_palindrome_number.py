# https://leetcode.com/problems/palindrome-number/

class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False

		x = str(x)

		i = 0
		j = len(x) - 1

		while i <= j:
			if x[i] == x[j]:
				i += 1
				j -= 1
			else:
				return False

		return True

	def isPalindromeFaster(self, x: int) -> bool:
		x = str(x)
		return x == x[::-1]
