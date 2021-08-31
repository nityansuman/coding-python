# Import packages
from typing import Union
from singly_linked_list import Node


class LinkedListStack:
	"""Stack (last-in, first out) data structure implementation using singly linked list.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.top = None
		self.bottom = None
		self.size = 0

	def push(self, value: Union[int, float, str]) -> None:
		"""Method to push element in stack.

		Args:
			value (Union[int, float, str]): Value to be pushed into stack.
		"""
		node = Node(node_data=value)
		node.next = self.top
		self.top = node
		self.size += 1

	def pop(self) -> None:
		"""Method to pop top element from the stack.

		Raises:
			Exception: If stack is empty.
		"""
		if self.bottom.next is None:
			self.top = None
			self.bottom = None

		btm = self.bottom

		while btm.next.next is not None:
			btm = btm.next

		btm.next = None
		self.top = btm

	def peek(self) -> Union[int, float, str]:
		"""Method to peek (view top element) into stack.

		Raises:
			Exception: If stack is empty.

		Returns:
			Union[int, float, str]: Top element of the stack.
		"""
		if self.bottom is None:
			raise Exception("Warning: Found empty stack.")

		return self.top.data

	def __repr__(self) -> str:
		"""Method that helps `print` the entire stack.

		Returns:
			str: String representation of the stack elements.
		"""
		values = list()
		btm = self.bottom

		while btm is not None:
			values.append(str(btm.data))
			btm = btm.next
		return ", ".join(values)


class DynamicArrayStack:
	"""Stack (last-in, first out) data structure implementation using dynamic arrays.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.stack = list()

	def push(self, value: Union[int, float, str]) -> None:
		"""Method to push element in stack.

		Args:
			value (Union[int, float, str]): Value to be pushed into stack.
		"""
		self.append(value)

	def pop(self) -> None:
		"""Method to pop top element from the stack.
		"""
		self.pop()

	def peek(self) -> Union[int, float, str]:
		"""Method to peek (view top element) into stack.

		Returns:
			Union[int, float, str]: Top element of the stack.
		"""
		return self.stack[-1]

	def size(self) -> int:
		"""Method to get the size of the stack.

		Returns:
			int: Size of the stack.
		"""
		return len(self.stack)

	def __repr__(self) -> str:
		"""Method that helps `print` the entire stack.

		Returns:
			str: String representation of the stack elements.
		"""
		return ", ".join([str(ele) for ele in self.stack])


if __name__ == "__main__":
	# Read inputs from stdin
	arr = list(map(int, input().strip().split()))

	# Create a dynamic array based stack
	# stack = DynamicArrayStack()

	# Create a linked based stack
	stack = LinkedListStack()

	for element in arr:
		stack.push(element)

	# View entire stack
	print("Stack:", stack)

	# Peek at the top element now
	print("Top element in the stack:", stack.peek())

	# # Delete the last element
	stack.pop()
	print("Stack after deleting the top element:", stack)

	# Peek at the top element now
	print("Top element in the stack:", stack.peek())

	# Get the size
	print("Size of the stack:", stack.size())

	# Add a random valueber to the stack
	stack.push(10)
	print("Stack after adding new element:", stack)

	# Peek at the top element now
	print("Top element in the stack:", stack.peek())
