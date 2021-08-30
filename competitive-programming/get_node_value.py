
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        # Create a new node
        node = SinglyLinkedListNode(node_data)

        # Add node at tail
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep,):
    while node:
        print(node.data)
        node = node.next


def get_node(llist, positionFromTail):
    # Write your code here
    pass


if __name__ == "__main__":
    # Read numer of test cases integer from stdni
    tests = int(input().strip())

    # Iterate over test cases
    for tests_itr in range(tests):

        # Read integer input from stdin
        num_elements = int(input().strip())

        # Create `SinglyLinkedList` instance
        llist = SinglyLinkedList()

        # Iterate over `num_elements`
        for _ in range(num_elements):
            # Read input to insert into list from stdin
            item = int(input().strip())

            # Insert element into list
            llist.insert_node(item)

        # Read position input from stdin
        position = int(input().strip())

        # Get node value for the `position`
        result = get_node(llist.head, position)
