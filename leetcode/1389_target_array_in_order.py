# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List


class Solution:
	def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
		output = list()

		for i in range(len(index)):
			output.insert(index[i], nums[i])

		return output
