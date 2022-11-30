# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		prod = 1
		total = 0

		for num in list(str(n)):
			prod *= int(num)
			total += int(num)

		return prod - total
