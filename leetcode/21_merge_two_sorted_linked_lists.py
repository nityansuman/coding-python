# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next


class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

		if list1 is None:
			return list2

		if list2 is None:
			return list1

		if list1.val < list2.val:
			curr = list1
			list1 = list1.next
		else:
			curr = list2
			list2 = list2.next

		head = curr

		while list1 and list2:
			if list1.val < list2.val:
				curr.next = list1
				list1 = list1.next
				curr = curr.next
			else:
				curr.next = list2
				list2 = list2.next
				curr = curr.next

		if list1 or list2:
			curr.next = list1 if list1 else list2

		return head
