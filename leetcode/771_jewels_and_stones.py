# https://leetcode.com/problems/jewels-and-stones/

class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		counter = 0

		for stone in stones:
			if stone in jewels:
				counter += 1

		return counter
