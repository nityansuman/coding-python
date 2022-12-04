# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List


class Solution:
	def mostWordsFound(self, sentences: List[str]) -> int:
		return max([len(sent.split()) for sent in sentences])

	def mostWordsFoundAlternate(self, sentences: List[str]) -> int:
		return max([sent.count(" ")+1 for sent in sentences])
