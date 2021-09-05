class SinglyLinkedListNode:
	"""Node class implementation.
	"""

	def __init__(self, node_data):
		self.data = node_data
		self.next = None


class SinglyLinkedList:
	"""Singly linked list class implementation.
	"""

	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		# Create a new node
		node = SinglyLinkedListNode(node_data)

		if not self.head:
			# Add ndoe to head when list is empty
			self.head = node
		else:
			# Add node to tail when list is not empty
			self.tail.next = node

		# Set new node as tail
		self.tail = node


def get_node(head, pos_from_tail):
	# Count number of nodes in the list
	num_nodes = 0

	curr = head
	while curr:
		num_nodes += 1
		curr  = curr.next

	# Now identify the node relative to tail
	pos_from_head = 0

	curr = head
	while pos_from_head + pos_from_tail + 1 < num_nodes:
		curr = curr.next
		pos_from_head += 1

	return curr.data


if __name__ == "__main__":
	# Read numer of test cases from stdin
	tests = int(input().strip())

	# For each test case
	for t in range(tests):
		# Read number of elements from stdin
		num_elements = int(input().strip())

		# Initiate singly linked list class
		llist = SinglyLinkedList()

		# For each element
		for _ in range(num_elements):
			# Read list input from stdin
			item = int(input().strip())

			# Insert input into list
			llist.insert_node(item)

		# Read position relative to tail from stdin
		position = int(input().strip())

		# Get data stored at node for the given position
		node_value = get_node(llist.head, position)
		print("Node Value:", node_value)
