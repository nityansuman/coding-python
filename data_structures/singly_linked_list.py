# Singly Linked List (a.k.a Linked List) Implementation

class Node:
	"""Node implementation.
	"""

	def __init__(self, value) -> None:
		"""Class constructor.

		Args:
			value (_type_): Value associated with each node.
		"""
		self.value = value
		self.next = None


class SinglyLinkedList:
	"""Singly linked list implementation.
	"""

	def __init__(self) -> None:
		"""Class constructor.
		"""
		self.head = None

	def insert_at_head(self, value) -> None:
		"""Method to insert node at the head of the linked list.

		Args:
			value (_type_): Value to be inserted at the head of the linked list.
		"""
		if self.head is None:
			self.head = new_node
			return

		new_node = Node(value=value)
		new_node.next = self.head
		self.head = new_node

	def insert_at_tail(self, value) -> None:
		"""Method to insert node at the tail of the linked list.

		Args:
			value (_type_): Value to be inserted at the tail of the linked list.
		"""
		if self.head is None:
			self.insert_at_head(value=value)
			return

		curr = self.head
		while curr.next is not None:
			curr = curr.next

		curr.next = Node(value=value)

	def insert_at_position(self, value, position) -> None:
		"""Method to insert aa node with associated value at a `position`.

		Args:
			value (_type_): Value to be inserted in the linked list.
			position (_type_): Position (positive integer) at which a value is to be inserted.

		Raises:
			ValueError: If `position` is greater than the actual size of the linked list.
		"""
		assert position >= 0

		if self.get_size() < position:
			raise ValueError("Invalid position.")

		if position == 0:
			self.insert_at_head(value=value)
			return

		curr = self.head
		count = 0
		while count != position-1:
			curr = curr.next
			count += 1

		new_node = Node(value)
		new_node.next = curr.next
		curr.next = new_node

	def delete_at_position(self, position: int) -> None:
		"""Method to delete value at `position` from the linked list.

		Args:
			position (int): Position (postive integer) for which value has to be deleted.

		Raises:
			ValueError: If `position` is greater than the actual size of the linked list or empty linked list.
		"""
		assert position >= 0

		if self.get_size() < position or self.is_empty():
			raise ValueError("Invalid position. Cannot delete.")

		if position == 0:
			self.head = self.head.next
			return

		count = 0
		curr = self.head
		while count != position-1:
			curr = curr.next
			count += 1

		curr.next = curr.next.next

	def reverse(self) -> None:
		"""Method to reverse the linked list.
		"""
		if self.is_empty():
			return 0

		prev = None
		curr = self.head

		while curr is not None:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node

		self.head = prev

	def is_empty(self) -> bool:
		"""Method to check if the linked list is empty.

		Returns:
			bool: Returns a boolean `True` if empty, `False` otherwise.
		"""
		if self.head is None:
			return True

		return False

	def get_size(self) -> int:
		"""Method to count the number of nodes in the linked list/

		Returns:
			int: Returns the count of number of nodes.
		"""
		if self.is_empty():
			return 0

		count = 0
		curr = self.head
		while curr is not None:
			count += 1
			curr = curr.next

		return count
