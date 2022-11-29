"""
Objective
	Today we're working with Linked Lists.
	A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).
	A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer data value that must be added to the end of the list as a new Node object.

Task
	A removeDuplicates function is declared in your editor, which takes a pointer to the next node of a linked list as a parameter.
	Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.
	Note: The next pointer may be null, indicating that the list is empty.
	Be sure to reset your next pointer when performing deletions to avoid breaking the list.

Input Format
	The first line contains an integer, N, the number of nodes to be inserted.
	The N subsequent lines each contain an integer describing the data value of a node being inserted at the list's tail.

Constraints
	The data elements of the linked list argument will always be in non-decreasing order.

Output Format
	Your removeDuplicates function should return the head of the updated linked list.
	The locked stub code in your editor will print the returned list to stdout.

Sample Input
	6
	1
	2
	2
	3
	3
	4

Sample Output
	1 2 3 4
"""


# Base node object class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Main solution class which implements linked list
class LinkedList:
    # Method to insert a new element at the tail of the linked list
	def insert(self, head, data):
		if head != None:
			# Non-empty linked list
			current = head
			# Traverse till last node
			while current.next != None:
				current = current.next
			# Create new node
			new_node = Node(data)
			# Point tails pointer to the new node
			current.next = new_node
		else:
			# Empty linked list
			new_node = Node(data)
			head = new_node
		# Return pointer to head
		return head

    # Method to display the elements from the list in order (head to tail)
	def display(self, head):
		current = head
		# Traverse through the linked list and print elements
		while current:
			print(current.data, end=' ')
			current = current.next

	# Method to remove any duplicates from the linked list
	def removeDuplicates(self, head):
		# In case of empty linked list
		if head == None:
			return head

		# Store head for return
		current = head

		while current.next != None:
			# See if next node has same data as current node
			if current.data == current.next.data:
				# Skip join the link and stay at the same node to check if further duplicates
				current.next = current.next.next
			else:
				# Move forward
				current = current.next
		return head


#  Entry point of the program
if __name__ == "__main__":
	# Initiate class
	my_linked_list = LinkedList()

	# Read number of nodes in linked list
	T = int(input())

	# Enter elemends/data into linked list
	head = None
	for i in range(T):
		# Read data in order
		data = int(input())
		# Add node to the linked list
		head = my_linked_list.insert(head, data)

	# Now remove duplicates from the created linked list
	head = my_linked_list.removeDuplicates(head)

	# Display the clean linked list
	my_linked_list.display(head)