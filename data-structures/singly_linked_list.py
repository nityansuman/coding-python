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
	"""Single linked list implementation with head pointer.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.head = None


# Complete the insert_at_head function below
def insert_at_head(head, data):
	# Create a new node
	node = Node(data)

	if head is None:
		# Empty linked list
		head = node
		return head

	# Link node to head
	node.next = head

	# Make node head
	head = node
	return head


# Complete the insert_at_tail function below
def insert_at_tail(head, data):
	# Create a new node
	node = Node(data)

	last = head

	if head is None:
		# Empty linked list
		head = node
		return head

	# Iterate to last node
	while last.next:
		last = last.next

	# Add node
	last.next = node
	return head


# Complete the insert_at_position function below
def insert_at_position(head, data, position):
	# Create a new node
	node = Node(data)

	if head is None:
		# Empty linked list
		head = node
		return head

	start = 0
	tail = head

	# Iterate to desired position
	while start != position-1:
		start += 1
		tail = tail.next

	# Add link to next node
	node.next = tail.next

	# Link current node to new node
	tail.next = node
	return head


# Complete the 'delete_at_position' function below
def delete_at_position(head, position):
	if not head:
		# Empty linked list
		return head

	if position == 0:
		# Delete at first position
		head = head.next
		return head

	# Iterate to any position starting 1
	tail = head
	start = 0
	while start != position-1:
		start += 1
		tail = tail.next

	# Now delete
	tail.next = tail.next.next
	return head


# Complete the 'reverse' function below
def reverse(head):
	previous = None
	current = head

	while current is not None:
		# Point to the next node
		next_node = current.next

		# Change pointer
		current.next = previous

		# Rename nodes
		previous = current
		current = next_node

		# Note: At end of each loop we have previous, current and next node
	# Note: Current would be none for last node
	head = previous
	return head
