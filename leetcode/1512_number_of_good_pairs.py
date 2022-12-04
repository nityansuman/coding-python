# https://leetcode.com/problems/number-of-good-pairs/

from typing import List


class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		counter = 0
		length = len(nums)

		for i in range(length):
			for j in range(i+1, length):
				if nums[i] == nums[j]:
					counter += 1
				else:
					continue

		return counter

	def numIdenticalPairsBetter(self, nums: List[int]) -> int:
		counter = 0
		seen = dict()

		for num in nums:
			if num not in seen:
				seen[num] = 1
			else:
				seen[num] += 1

		for num in seen:
			if seen[num] > 1:
				val = seen[num]
				counter += ((val-1) * val) // 2

		return counter
