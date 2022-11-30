
class Solution:

	def __init__(self):
		self.stack = list()
		self.queue = list()

	# Method to push elements into the stack
	def push_character(self, c):
		self.stack.append(c)

	# Method to pop out elements from the stack
	def pop_character(self):
		return self.stack.pop(-1)

	# Method to enter element into the queue
	def enqueue_character(self, c):
		self.queue.append(c)

	# Method to remove element from the queue
	def dequeue_character(self):
		return self.queue.pop(0)


if __name__ == "__main__":
	# Read input string from stdin
	s = input()

	# Create the Solution class object
	obj = Solution()

	# Iterate over the string
	for i, v in enumerate(s):
		obj.push_character(v)
		obj.enqueue_character(v)

	# Set palindrome flag
	is_palindrome = True

	for i in range(len(s) // 2):
		if obj.pop_character() != obj.dequeue_character():
			is_palindrome = False
			break

	# Finally print whether string s is palindrome or not.
	if is_palindrome:
		print("The word, "+s+", is a palindrome.")
	else:
		print("The word, "+s+", is not a palindrome.")
