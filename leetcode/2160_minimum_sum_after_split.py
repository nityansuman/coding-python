# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
	def minimumSum(self, num: int) -> int:
		nums = sorted(str(num))
		return int(nums[0])*10 + int(nums[2]) + int(nums[1])*10 + int(nums[3])
