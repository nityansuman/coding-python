
class Node:
	def __init__(self, data):
		# Each node has `data` and `next` pointer placeholder
		self.data = data
		self.next = None


class MyList:
	def display(self, head):
		# Set current to point to head
		current = head

		# Traverse till last node
		while current is not None:
			# Print data
			print(current.data, end=" ")

			# Move to next node
			current = current.next

	def insert_at_tail(self, head, data):
		if head != None:
			# Non-empty linked list

			# Set current to point to head
			current = head

			# Traverse till last node
			while current.next != None:
				current = current.next

			# Create new node
			new_node = Node(data)

			# Point tails to the new node
			current.next = new_node
		else:
			# Empty linked list

			# Create new node
			new_node = Node(data)

			# Set head to new node
			head = new_node

		# Return head
		return head


if __name__ == "__main__":
	# Create an instance of custom list implementation
	a_list = MyList()

	# Read test case input from stdin
	T = int(input())

	# Set `head` to None
	head = None

	# Iterate over the range `T`
	for i in range(T):
		# Read input data from stdin to insert in the list
		data = int(input())

		# Insert data to list
		head = a_list.insert_at_tail(head, data)

	# Display the list content
	a_list.display(head)
