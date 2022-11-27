# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		empty_space = list()
		seen = dict()

		counter = 0

		for i in range(len(nums)):
			if nums[i] not in seen:
				seen[nums[i]] = i
				counter += 1

				if empty_space:
					nums[empty_space[0]] = nums[i]
					empty_space.remove(empty_space[0])
					empty_space.append(i)
			else:
				empty_space.append(i)

		return counter
