# Data class
class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

# Custom List class
class MyList:
	def insert(self, head, data):
		p = Node(data)

		if head == None:
			# No nodes
			head = p
		elif head.next == None:
			# Single node
			head.next = p
		else:
			# More than 1 nodes
			curr = head
			while curr.next != None:
				curr = curr.next
			curr.next = p
		return head

	def display(self, head):
		# Iterate over all nodes from head
		curr = head
		while curr:
			print(curr.data, end=" ")
			curr = curr.next
		print()

	def remove_duplicates(self, head):
		if head == None:
			# If no node
			return head

		# When more than 1 node
		curr = head
		while curr.next != None:
			# Check for duplicates
			if curr.data == curr.next.data:
				curr.next = curr.next.next
			else:
				curr = curr.next
		return head


if __name__ == "__main__":
	# Read input integer from stdin
	num_test_cases = int(input())

	# Instantiate list class
	my_list = MyList()

	# Set `head` pointer to None
	head = None

	# Iteratively insert node
	for i in range(num_test_cases):
		# Read data input integer from stdin
		data = int(input())
		# Insert data as node
		head = my_list.insert(head, data)

	# Display list
	print("List with duplicates:")
	my_list.display(head)

	# Remove duplicates from list
	head = my_list.remove_duplicates(head)

	# Display list again
	print("List without duplicates:")
	my_list.display(head)
