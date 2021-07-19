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

	def insert_at_head(self, data: Union[int, float, str]) -> None:
		"""Method to insert element at head.

		Args:
			data (Union[int, float, str]): Data to be added to linked list at head.
		"""
		# Create a new node
		node = Node(data)

		if self.head is None:
			# Empty linked list
			self.head = node
			return self.head

		# Link node to self.head
		node.next = self.head

		# Make node self.head
		self.head = node

	def insert_at_tail(self, data: Union[int, float, str]) -> None:
		"""Method to insert element at tail.

		Args:
			data (Union[int, float, str]): Data to be added to linked list at tail.
		"""
		# Create a new node
		node = Node(data)

		last = self.head

		if self.head is None:
			# Empty linked list
			self.head = node
			return self.head

		# Iterate to last node
		while last.next:
			last = last.next

		# Add node
		last.next = node

	def insert_at_position(self, data: Union[int, float, str], position: int) -> None:
		"""Method to insert data at a position.

		Args:
			data (Union[int, float, str]): Data to be added to linked list.
			position (int): Position at which data (node) is to be inserted.
		"""
		# Create a new node
		node = Node(data)

		if self.head is None:
			# Empty linked list
			self.head = node
			return True

		temp_head = self.head

		if position == 0:
			node.next = temp_head
			self.head = node
			return True

		start = 0
		# Iterate to desired position
		while start != position-1:
			start += 1
			temp_head = temp_head.next

		# Add link to next node
		node.next = temp_head.next

		# Link current node to new node
		temp_head.next = node

	def delete_at_position(self, position: int) -> None:
		"""Method to remove data (node) at a position.

		Args:
			position (int): Position at which data (node) is to be deleted.
		"""
		if not self.head:
			# Empty linked list
			raise Exception("Empty LinkedList, Cannot delete.")

		if position == 0:
			# Delete at first position
			self.head = self.head.next
			return True

		# Iterate to any position starting 1
		tail = self.head
		start = 0
		while start != position-1:
			start += 1
			tail = tail.next

		# Now delete
		tail.next = tail.next.next

	def reverse(self):
		"""Method to reverse the linked list.
		"""
		previous = None
		current = self.head

		while current is not None:
			# Point to the next node
			next_node = current.next

			# Change pointer
			current.next = previous

			# Rename nodes
			previous = current
			current = next_node

		self.head = previous

	def __repr__(self) -> str:
		"""Method that helps `print` the entire linked list.

		Returns:
			str: String representation of the linked list elements.
		"""
		values = list()
		btm = self.head

		while btm is not None:
			values.append(str(btm.data))
			btm = btm.next
		return " -> ".join(values)


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
