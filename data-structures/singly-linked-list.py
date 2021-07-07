
# Node
class SinglyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None


# Linked list
class SinglyLinkedList:
	def __init__(self):
		self.head = None


# Complete the insert_at_head function below
def insert_at_head(head, data):
	# Create a new node
	node = SinglyLinkedListNode(data)

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
	node = SinglyLinkedListNode(data)

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
	node = SinglyLinkedListNode(data)

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



# if __name__ == "__main__":
# 	llist_count = int(input())
# 	llist = SinglyLinkedList()

# 	# Part 1: Insert at `Head`
# 	for i in range(llist_count):
# 		llist_item = int(input())
# 		llist_head = insert_at_head(llist.head, llist_item)
# 		llist.head = llist_head

# 	# Part 2: Inser at `Tail`
# 	for i in range(llist_count):
# 		llist_item = int(input())
# 		llist_head = insert_at_tail(llist.head, llist_item)
# 		llist.head = llist_head

# 	# Part 3: Insert at a position
# 	for _ in range(llist_count):
# 		llist_item = int(input())
# 		llist.insert_node(llist_item)

# 	data = int(input())
# 	position = int(input())
# 	llist_head = insert_at_position(llist.head, data, position)

# 	# Part 4: Delete at a position
# 	position = int(input())
# 	llist1 = delete_at_position(llist.head, position)

# 	# Part 5: Reverse a linked list
# 	new_llist = reverse(llist.head)
