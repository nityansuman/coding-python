# https://leetcode.com/problems/ransom-note/

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		if len(magazine) < len(ransomNote):
			return False

		ransom_mapping = {k:ransomNote.count(k) for k in set(ransomNote)}
		mapping = {k:magazine.count(k) for k in set(magazine)}

		for k in ransom_mapping:
			if k not in mapping:
				return False
			else:
				if mapping[k] < ransom_mapping[k]:
					return False

		return True

	def canConstructFaster(self, ransomNote: str, magazine: str) -> bool:
		for ch in set(ransomNote):
			if ransomNote.count(ch) > magazine.count(ch):
				return False
		return True
