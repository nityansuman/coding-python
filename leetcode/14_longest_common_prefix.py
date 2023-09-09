# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if len(strs) == 1:
			return strs[0]

		prefix = ""
		for i in range(len(strs) - 1):
			s1 = strs[i]
			s2 = strs[i+1]

			if len(s1) == 0 or len(s2) == 0:
				return ""

			j = 0
			while j < len(s1) and j < len(s2):
				if s1[j] == s2[j]:
					j += 1
				else:
					break

			if j >= 1:
				if prefix == "" or s1[0:j] in prefix:
					prefix = s1[0:j]
			else:
				return ""

		return prefix

	def longestCommonPrefixAlternate(self, strs: List[str]) -> str:
		shortest = min(strs, key=len)

		for i, char in enumerate(shortest):
			for str in strs:
				if str[i] != char:
					return shortest[:i]

		return shortest
