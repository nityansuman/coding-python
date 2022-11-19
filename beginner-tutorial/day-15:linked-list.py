"""
Objective
	Today we're working with Linked Lists.
	A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).
	A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer data value that must be added to the end of the list as a new Node object.

Task
	Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the first (head) node.
	Note: If the data argument passed to the insert function is null, then the initial list is empty.

Input Format
	The insert function has 2 parameters: a pointer to a Node named head, and an integer value, data.
	The constructor for Node has 1 parameter: an integer value for the data field.

Output Format
	Your insert function should return a reference to the  node of the linked list.

Sample Input
	The first line contains T, the number of test cases.
	The T subsequent lines of test cases each contain an integer to be inserted at the list's tail.
	4
	2
	3
	4
	1

Sample Output
	Print the elements of the list from head to tail separated by a single space.
	2 3 4 1
"""


# Base node class
class Node:
	# Class constructor
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution class
class Solution:
	# Class constructor
	def __init__(self):
		# Does nothing
		pass

	# Method to display the elements from the list in order (head to tail)
    def display(self, head):
        current = head
		# Traverse through the linked list and print elements
        while current:
            print(current.data, end=' ')
            current = current.next

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


# Entry point of the program
if __name__ == "__main__":
	# Initiate class
	mylist = Solution()

	# Read input for number of test cases
	T = int(input())

	# Create linked list from the next T input integers as elements
	head = None
	for i in range(T):
		data = int(input())
		head = mylist.insert(head, data)

	# Display elements of the linked list in order
	mylist.display(head)