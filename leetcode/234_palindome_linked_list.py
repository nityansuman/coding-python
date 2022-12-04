# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if head.next is None:
			return True

		num = ""
		while head:
			num += str(head.val)
			head = head.next

		return num == num[::-1]
