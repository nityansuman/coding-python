# Import packages
from typing import Union


class DynamicArrayQueue:
	"""Queue (first-in, first out) data structure implementation using dynamic arrays.
	"""

	def __init__(self) -> None:
		"""Constructor.
		"""
		self.queue = list()

	def enqueue(self, value: Union[int, float, str]) -> None:
		"""Method to add element to a queue.

		Args:
			value (Union[int, float, str]): Value to be pushed into queue.
		"""
		self.queue.append(value)

	def dequeue(self) -> None:
		"""Method to remove first element from the queue.
		"""
		for i in range(1, len(self.queue)):
			self.queue[i-1] = self.queue[i]
		self.queue.pop()

	def size(self) -> int:
		"""Method to get the size of the queue.

		Returns:
			int: Size of the queue.
		"""
		return len(self.queue)

	def __repr__(self) -> str:
		"""Method that helps `print` the entire queue.

		Returns:
			str: String representation of the queue elements.
		"""
		return ", ".join([str(ele) for ele in self.queue])


# Test
if __name__ == "__main__":
	# Read inputs from stdin
	arr = list(map(int, input().strip().split()))

	# Create a dynamic array based queue
	queue = DynamicArrayQueue()

	# Add elements to queue
	for element in arr:
		queue.enqueue(element)

	# View entire queue
	print("Queue:", queue)

	# Get size of queue
	print("Size of the queue:", queue.size())

	# Delete first element
	queue.dequeue()
	print("Queue after deleting the top element:", queue)

	# Get size of queue
	print("Size of the queue:", queue.size())
