# https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
	def shuffle(self, nums: List[int], n: int) -> List[int]:
		shuffled_arr = list()
		i = 0
		while i < n:
			shuffled_arr.extend((nums[i], nums[i+1]))
			i += 1

		return shuffled_arr

# Note:
# 1. Extend better than multiple appens
# 2. List creation more expensive than tuple
