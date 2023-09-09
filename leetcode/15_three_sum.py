# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
# https://leetcode.com/problems/3sum/description/

from typing import List, Tuple

class Solution:
	def twoSum(self, nums: List[int], index: int, target: int, base: int) -> Tuple[int]:
		seen = dict()
		output = list()

		for i, num in enumerate(nums):
			if i != index:
				if target - num in seen:
					output.append(sorted((base, num, seen[target - num])))
				else:
					seen[num] = num

		return output

	def threeSum(self, nums: List[int]) -> List[List[int]]:
		three_sum_list = list()

		for i, n in enumerate(nums):
			output = self.twoSum(nums=nums, index=i, target=0-n, base=n)

			for out in output:
				if out not in three_sum_list:
					three_sum_list.append(out)

		return three_sum_list
