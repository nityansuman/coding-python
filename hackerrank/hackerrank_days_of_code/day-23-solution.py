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

	def level_order_traversal(self, root):
		queue = list()

		# Enqueue and print root (first node)
		queue.append(root)
		print(root.data, end=" ")

		# Access all nodes level wise
		while len(queue) != 0:
			# Dequeue
			v = queue.pop(0)

			# If left sub-tree is present, traverse
			if v.left != None:
				# Enqueue and print
				queue.append(v.left)
				print(v.left.data, end=" ")

			# If right sub-tree is present, traverse
			if v.right != None:
				# Enqueue and print
				queue.append(v.right)
				print(v.right.data, end=" ")


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

	# Traverse tree level wise
	tree_instance.level_order_traversal(root)
