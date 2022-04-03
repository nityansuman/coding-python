# Import packages
from typing import Iterable, Union


class Node:
	"""Node construct.

	Each node has two components:
		`data`: Value.
		`next`: Link to next node.
	"""

	def __init__(self, data: Union[int, float, str, Iterable]) -> None:
		"""Node constructor.

		Args:
			data (Union[int, float, str, Iterable]): Value to be assigned to the node.
		"""
		self.data = data
		self.next = None


class Stack:
	"""Stack (LIFO = Last In First Out) class implementation using singly linked list.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.top = None

	def is_empty(self) -> bool:
		"""Method to check if stack is empty.

		Returns:
			bool: Return True if empty else False.
		"""
		if self.top is None:
			return True

		return False

	def push(self, value: Union[int, float, str, Iterable]) -> None:
		"""Method to push element in the stack.

		Args:
			value (Union[int, float, str]): Value to be pushed into stack.
		"""
		# Create node
		node = Node(data=value)

		# Add node to top of stack
		node.next = self.top

		# Make current node as top
		self.top = node

	def pop(self) -> None:
		"""Method to pop out element from top of stack.
		"""
		# Check if stack is empty
		if self.is_empty():
			return None

		# Shift top element to next node
		popped_node = self.top
		self.top = self.top.next

		# Remove link
		popped_node.next = None

		# Return popped element
		return popped_node.data

	def peek(self) -> Union[int, float, str, Iterable]:
		"""Method to view top element of the stack.

		Returns:
			Union[int, float, str, Iterable]: Top element of the stack.
		"""
		# Check if stack is empty
		if self.is_empty():
			return None

		# If stack not empty, return top element
		return self.top.data

	def __repr__(self) -> str:
		"""Method to construct string representation of the entire stack.
		This string representation is used by `print`.

		Returns:
			str: String representation of the stack elements.
		"""
		# Check if stack is empty
		if self.is_empty():
			return None

		str_repr = "\n"
		curr = self.top

		# Iterate and create a string representation
		while curr.next is not None:
			str_repr += "|" + str(curr.data) + "|\n"
			curr = curr.next

		str_repr += "|" + str(curr.data) + "|"
		return str_repr


if __name__ == "__main__":
	# Read inputs from stdin
	arr = list(map(int, input().strip().split()))

	# Create a linked based stack
	stack = Stack()

	for element in arr:
		stack.push(element)

	# Check if stack is empty
	print("Is Stack empty:", stack.is_empty())

	# View entire stack
	print("Stack:", stack)

	# Peek at the top element now
	print("Top element in the stack:", stack.peek())

	# Remove top element from stack
	popped_element = stack.pop()
	print("Stack after deleting the top element:", stack)
	print("Popped element from stack = ", popped_element)

	# Peek at the top element now
	print("Top element in the stack:", stack.peek())
