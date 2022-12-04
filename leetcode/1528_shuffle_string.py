# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
	def restoreString(self, s: str, indices: List[int]) -> str:
		return "".join([t[1] for t in sorted(tuple(zip(indices, s)))])
