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
		while l1 is not None:
			str1 += str(l1.val)
			l1 = l1.next

		str2 = ""
		while l2 is not None:
			str2 += str(l2.val)
			l2 = l2.next

		val = str(int(str1[::-1]) + int(str2[::-1]))[::-1]

		node = ListNode(val=val[0])

		h = node
		for c in val[1:]:
			temp_node = ListNode(val=c)
			node.next = temp_node
			node = temp_node

		return h
