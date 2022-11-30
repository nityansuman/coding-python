# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List

class Solution:
	def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
		max_candies = max(candies)
		output = list()

		for candy in candies:
			if candy + extra_candies >= max_candies:
				output.append(True)
			else:
				output.append(False)

		return output
