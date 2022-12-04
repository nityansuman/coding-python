# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		return [sum(nums[:i+1]) for i in range(len(nums))]
