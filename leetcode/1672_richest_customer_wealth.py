# https://leetcode.com/problems/richest-customer-wealth/

from typing import List


class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		max_wealth = 0

		for customer in accounts:
			wealth = sum(customer)
			if wealth > max_wealth:
				max_wealth = wealth

		return max_wealth
