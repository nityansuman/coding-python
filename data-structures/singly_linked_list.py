from typing import Union


class Node:
	"""Node implementation for linked list.

	Each node has two components:
		`data`: Value component
		`next`: Link component
	"""

	def __init__(self, node_data: Union[int, float, str]) -> None:
		"""Constructor.

		Args:
			node_data (Union[int, float, str]): Value to be assigned to the node.
		"""
		self.data = node_data
		self.next = None


class SinglyLinkedList:
	"""Single linked list implementation with self.head pointer.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.head = None
		self.size = 0

	def insert_at_head(self, data: Union[int, float, str]) -> None:
		"""Method to insert element at the begining of the linked list.

		Args:
			data (Union[int, float, str]): Data to be added to linked list at head.
		"""
		node = Node(data)
		node.next = self.head
		self.head = node
		self.size += 1

	def insert_at_tail(self, data: Union[int, float, str]) -> None:
		"""Method to insert element at tail.

		Args:
			data (Union[int, float, str]): Data to be added to linked list at tail.
		"""
		node = Node(data)

		if self.head is None:
			node.next = self.head
			self.head = node
			self.size += 1
			return

		cur = self.head
		while cur.next is not None:
			cur = cur.next

		cur.next = node
		self.size += 1

	def insert_at_position(self, data: Union[int, float, str], position: int) -> None:
		"""Method to insert data at a position.

		Args:
			data (Union[int, float, str]): Data to be added to linked list.
			position (int): Position at which data (node) is to be inserted.
				Position value here starts from 0.
		"""
		if self.is_empty():
			raise Exception("Found empty `SinglyLinkedList`.")

		if self.get_size() < position or position < 0:
			raise Exception("Incorrect position.")

		node = Node(data)

		if position == 0:
			node.next = self.head
			self.head = node
			self.size += 1
			return

		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		node.next = cur.next
		cur.next = node

	def delete_at_position(self, position: int) -> None:
		"""Method to remove data (node) at a position.

		Args:
			position (int): Position at which data (node) is to be deleted.
		"""
		if self.is_empty():
			raise Exception("Found empty `SinglyLinkedList`.")

		if self.get_size() < position or position < 0:
			raise Exception("Incorrect position.")

		if position == 0:
			self.head = self.head.next
			self.size -= 1
			return

		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		cur.next = cur.next.next

	def reverse(self):
		"""Method to reverse the linked list.
		"""
		if self.is_empty():
			raise Exception("Found empty `SinglyLinkedList`.")

		prev = None
		cur = self.head

		while cur is not None:
			next_node = cur.next
			cur.next = prev
			prev = cur
			cur = next_node

		self.head = prev

	def is_empty(self) -> bool:
		"""Method to find if the instance of `SinglyLinkedList` is empty or not.

		Returns:
			bool: True if empty else False.
		"""
		return self.size == 0

	def get_size(self) -> int:
		"""Method to get the size of the linked list.

		Returns:
			int: Integer denoting the size of the linked list.
		"""
		return self.size

	def __repr__(self) -> str:
		"""Method that helps `print` the entire linked list.

		Returns:
			str: String representation of the linked list elements.
		"""
		output = ""
		cur = self.head

		while cur is not None:
			output += str(cur.data) + " -> "
			cur = cur.next
		return output[:-3]


# Test
if __name__ == "__main__":
	# Read inputs from stdin
	arr = list(map(int, input("Elements (add at tail):").strip().split()))

	# Create a linked list
	linked_list = SinglyLinkedList()

	# Add elements to the list
	for element in arr:
		linked_list.insert_at_tail(element)

	# View linked list elements
	print("Linked List:", linked_list)

	# Read another set of inputs from stdin
	arr = list(map(int, input("Elements (add at head):").strip().split()))

	# Add elements to the list
	for element in arr:
		linked_list.insert_at_head(element)

	# View linked list elements
	print("Updated Linked List:", linked_list)

	# Read input from stdin to add at a position
	arr = list(map(int, input("Element - Position (add at position):").strip().split()))

	# Add element at a position
	linked_list.insert_at_position(data=arr[0], position=arr[1])

	# View linked list elements
	print("Linked List after additon:", linked_list)

	# Add element at a position
	linked_list.delete_at_position(position=arr[1])

	# View linked list elements
	print("Linked List after deletion:", linked_list)

	# Revers linked list
	linked_list.reverse()

	# View linked list elements
	print("Reversed Linked List:", linked_list)
