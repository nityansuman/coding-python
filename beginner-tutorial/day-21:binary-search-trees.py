"""
Objective
	Today, we're working with Binary Search Trees (BSTs).

Task
	The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
	You are given a pointer, root, pointing to the root of a binary search tree. Write BST tree using classes and implement a method called `get_height` returns the height of the binary search tree on input of the root of the BST.

Input Format
	The first line contains an integer, n, denoting the number of nodes in the tree.
	Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

Output Format
	Print the integer returned by `get_height` function denoting the height of the BST.

Sample Input
	7
	3
	5
	2
	1
	4
	6
	7

Sample Output
3
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

    def get_height(self, root):
		# Method to compute height of the BST
        if root == None:
            return -1
        else:
			# Compute left and right sub-tree height
            left_height = self.get_height(root.left)
            right_height = self.get_height(root.right)

			# Return based on larger sub-tree
            if left_height >= right_height:
                return 1 + left_height
            else:
                return 1 + right_height


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

	# Compute height of the BST
	height = my_tree.get_height(root)
	print(height)