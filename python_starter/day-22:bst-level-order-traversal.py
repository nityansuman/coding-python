"""
Objective
	Today, we're going further with Binary Search Trees.

Task
	A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom.
	You are given a pointer, root, pointing to the root of a binary search tree.
	Implement a BST class to insert elements and create a BST.
	Also implement `levelOrder` function so that it prints the level-order traversal of the binary search tree.
	Hint: You'll find a queue helpful in completing this challenge.

Input Format
	The first line contains an integer, T (the number of test cases).
	The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.

Output Format
	Print the data value of each node in the tree's level-order traversal as a single line of T-1 space-separated integers.

Sample Input
	6
	3
	5
	4
	7
	2
	1

Sample Output
	3 2 5 1 4 7
"""

# Base node class
class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data


# Base BST class
class BST:
	def __init__(self):
		# Class constructor does nothing
		pass

	def insert(self, root, data):
		# Method to insert element into the BST
		if root==None:
			return Node(data)
		else:
			if data <= root.data:
				# Insert of left
				cur = self.insert(root.left, data)
				# Point to new node
				root.left = cur
			else:
				# Insert of right
				cur = self.insert(root.right, data)
				# Poiint to new node
				root.right = cur
		return root

	def level_order_traversal(self, root):
		# Method to perform level order travesla, also know as breadth-first-search (BFS)
		queue = list()
		queue.append(root) # Enqueue
		print(root.data, end=" ")

		while len(queue) != 0:
			v = queue.pop(0) # Dequeue
			# Access both branches and print data
			if v.left != None:
				queue.append(v.left)
				print(v.left.data, end=" ")
			if v.right != None:
				queue.append(v.right)
				print(v.right.data, end=" ")



# Entry point of the program
if __name__ == "__main__":
	# Read integer input for number of elements in the BST
	T = int(input())

	# Intiate a BST
	my_tree = BST()

	# Read elements to insert into BST from stdin
	root = None
	for i in range(T):
		data = int(input())
		root = my_tree.insert(root, data)

	# Level order tree traversal
	my_tree.level_order_traversal(root)