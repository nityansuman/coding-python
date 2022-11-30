class Node:
	def __init__(self, node_data: int) -> None:
		self.data = node_data
		self.next = None

class SinglyLinkedList:
	def __init__(self) -> None:
		self.head = None
		self.tail = None

	def insert_node(self, node_data) -> None:
		node = Node(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node

		self.tail = node

def get_node(head, pos_from_tail) -> int:
	num_nodes = 0

	curr = head
	while curr:
		num_nodes += 1
		curr  = curr.next

	pos_from_head = 0

	curr = head
	while pos_from_head + pos_from_tail + 1 < num_nodes:
		curr = curr.next
		pos_from_head += 1

	return curr.data


if __name__ == "__main__":
	tests = int(input().strip())

	for t in range(tests):
		num_elements = int(input().strip())

		llist = SinglyLinkedList()

		for _ in range(num_elements):
			item = int(input().strip())
			llist.insert_node(item)

		position = int(input().strip())

		node_value = get_node(llist.head, position)
		print("Node Value:", node_value)
