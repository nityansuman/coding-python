# Stack Implementation Using Singly Linked List

class Node:

	def __init__(self, data: int) -> None:
		self.data = data
		self.next = None


class Stack:

	def __init__(self) -> None:
		self.top = None

	def is_empty(self) -> bool:
		if self.top is None:
			return True

		return False

	def push(self, value) -> None:
		node = Node(data=value)
		node.next = self.top
		self.top = node

	def pop(self) -> None:
		if self.is_empty():
			return None

		popped_node = self.top
		self.top = self.top.next
		popped_node.next = None

		return popped_node.data

	def peek(self) -> int:
		if self.is_empty():
			return None

		return self.top.data

	def __repr__(self) -> str:
		if self.is_empty():
			return None

		str_repr = "\n"
		curr = self.top

		while curr.next is not None:
			str_repr += "|" + str(curr.data) + "|\n"
			curr = curr.next

		str_repr += "|" + str(curr.data) + "|"
		return str_repr
