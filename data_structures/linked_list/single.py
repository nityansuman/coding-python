class Node:
	"""Node construct.

	Each node has two components:
		`value`: Value to be stored in the node.
		`next`: Link to the next node.
	"""

	def __init__(self, value) -> None:
		self.value = value
		self.next = None


class SinglyLinkedList:
	"""Singly linked list class implementation."""

	def __init__(self) -> None:
		self.head = None

	def insert_at_head(self, value) -> None:
		# Create a node
		node = Node(value=value)

		# Add node at head
		node.next = self.head

		# Set new node as head
		self.head = node

	def insert_at_tail(self, value) -> None:
		# If empty linked list
		if self.head is None:
			self.insert_at_head(value=value)
			return

		# If linked list is not empty
		# Iterate to the last node
		cur = self.head
		while cur.next is not None:
			cur = cur.next

		# Add node at tail
		node = Node(value=value)
		cur.next = node

	def insert_at_position(self, value, position) -> None:
		if self.get_size() < position or position < 0:
			raise ValueError("Invalid position value.")

		# Create a node
		node = Node(value)

		# Add node at head
		if position == 0:
			# Add node
			node.next = self.head
			self.head = node
			return

		# Iterate to node before the specified position
		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		# Add node at next position
		node.next = cur.next
		cur.next = node

	def delete_at_position(self, position) -> None:
		if self.is_empty():
			return None

		if self.get_size() < position or position < 0:
			return None

		# Delete node at head
		if position == 0:
			self.head = self.head.next
			return

		# Iterate to node before the specified position
		cur = self.head
		count = 0
		while count != position-1:
			cur = cur.next
			count += 1

		# Delete node
		cur.next = cur.next.next

	def reverse(self) -> None:
		if self.is_empty():
			return None

		# Set pointers
		prev = None
		cur = self.head

		# Iterate to the end of the list and revser node links
		while cur is not None:
			next_node = cur.next
			cur.next = prev
			prev = cur
			cur = next_node

		# Set tail as new head
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
	arr = list(
		map(int, input("Element - Position (add at position):").strip().split()))

	# Add element at a position
	linked_list.insert_at_position(value=arr[0], position=arr[1])

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
