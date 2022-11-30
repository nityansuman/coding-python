# Data class
class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data

# Tree class
class Tree:
	def insert(self, root, data):
		# If no root, create new root
		if root == None:
			return Node(data)
		else:
			# Insert a node in the present tree
			if data <= root.data:
				# If data is smaller or equal than root value
				cur = self.insert(root.left, data)
				root.left = cur
			else:
				# If data is greater than root value
				cur = self.insert(root.right, data)
				root.right = cur
		return root

	def get_height(self, root):
		# If no root
		if root == None:
			return -1
		else:
			# Iterate left and right sub-tree to compute height
			left_height = self.get_height(root.left)
			right_height = self.get_height(root.right)

			if left_height >= right_height:
				return 1 + left_height
			else:
				return 1 + right_height


if __name__ == "__main__":
	# Read input integer from stdin
	num_test_cases = int(input())

	# Instantiate tree class
	tree_instance = Tree()

	# Set `root` to None
	root = None

	# Iteratively insert node
	for i in range(num_test_cases):
		# Read data input integer from stdin
		data = int(input())
		# Insert data as node
		root = tree_instance.insert(root, data)

	# Compute height of the tree
	height = tree_instance.get_height(root)
	print("Height of the tree:", height)
