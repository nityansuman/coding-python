# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		l = 0
		r = len(nums) - 1

		while l <= r:
			mid = (l + r) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1

		if nums[mid] > target:
			return mid
		else:
			return mid + 1
