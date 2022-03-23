class Node:
	"""Node construct.

	Each node has two components:
		value: Value to be stored in the node.
		next: Link to the next node.
	"""

	def __init__(self, value) -> None:
		self.value = value
		self.next = None


class SinglyLinkedList:
	"""Singly linked list class implementation."""

	def __init__(self) -> None:
		self.head = None

	def insert_at_head(self, value) -> None:
		node = Node(value=value)
		node.next = self.head
		self.head = node

	def insert_at_tail(self, value) -> None:
		if self.head is None:
			self.insert_at_head(value=value)
			return

		cur = self.head
		while cur.next is not None:
			cur = cur.next

		node = Node(value=value)
		cur.next = node

	def insert_at_position(self, value, position) -> None:
		if self.get_size() < position or position < 0:
			raise ValueError("Invalid position value.")

		node = Node(value)

		if position == 0:
			node.next = self.head
			self.head = node
			return

		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		node.next = cur.next
		cur.next = node

	def delete_at_position(self, position) -> None:
		if self.is_empty():
			return None

		if self.get_size() < position or position < 0:
			return None

		if position == 0:
			self.head = self.head.next
			return

		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		cur.next = cur.next.next

	def reverse(self) -> None:
		if self.is_empty():
			return None

		prev = None
		cur = self.head

		while cur is not None:
			next_node = cur.next
			cur.next = prev
			prev = cur
			cur = next_node

		self.head = prev

	def is_empty(self) -> bool:
		if self.head is None:
			return True
		return False

	def get_size(self) -> int:
		count = 0

		if self.is_empty():
			return count

		curr = self.head
		while curr is not None:
			count += 1
			curr = curr.next

		return count

	def __repr__(self) -> str:
		return None
