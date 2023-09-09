# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		curr = head

		cnt = 0
		while curr != None:
			curr = curr.next
			cnt += 1

		if cnt % 2 != 0:
			middle = (cnt+1) // 2
		else:
			middle = (cnt // 2) + 1

		cnt = 0
		while cnt != middle-1:
			cnt += 1
			head = head.next

		return head

	def middleNodeBetter(self, head: Optional[ListNode]) -> Optional[ListNode]:
		fast = head
		slow = head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		return slow
