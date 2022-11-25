# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

		str1 = ""
		h1 = l1
		while h1 is not None:
			str1 += str(h1.val)
			h1 = h1.next

		str2 = ""
		h2 = l2
		while h2 is not None:
			str2 += str(h2.val)
			h2 = h2.next

		val = str(int(str1[::-1]) + int(str2[::-1]))
		val = val[::-1]

		node = ListNode(val=val[0])

		h = node
		for c in val[1:]:
			temp_node = ListNode(val=c)
			node.next = temp_node
			node = temp_node

		return h
