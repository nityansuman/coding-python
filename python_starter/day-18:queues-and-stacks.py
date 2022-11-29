"""
Objective
	Welcome to Day 18! Today we're learning about Stacks and Queues.

Task
	A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, s, is a palindrome?

	To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means s isn't a palindrome).

	Write the following declarations and implementations:
		Two instance variables: one for your stack, and one for your queue.
		A void push_character(char ch) method that pushes a character onto a stack.
		A void enqueue_character(char ch) method that enqueues a character in the queue instance variable.
		A char pop_character() method that pops and returns the character at the top of the stack instance variable.
		A char dequeue_character() method that dequeues and returns the first character in the queue instance variable.

Input Format
	You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string s. It then calls the methods specified above to pass each character to your instance variables.

Constraints
	s is composed of only lowercase English letters.

Output Format
	If your code is correctly written and s is a palindrome, then print `The word, $s, is a palindrome`; otherwise, print `The word, s, is not a palindrome`. The $ represent the variable here.

Sample Input
	racecar

Sample Output
	The word, racecar, is a palindrome.
"""


# Base class
class Solution:
	# Class constructor
	def __init__(self):
		# Instance variables for stack and queue using lists
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


# Entry point of the program
if __name__ == "__main__":
	# Read the string s
	s = input().strip()

	# Create the Solution class object
	obj = Solution()

	l = len(s)
	# Push/enqueue all the characters of string s to stack
	for i in range(l):
		obj.push_character(s[i])
		obj.enqueue_character(s[i])

	# Set flag
	is_palindrome = True

	# Check if it is a palindrome or not
	for i in range(l // 2):
		# Pop out character from stack and dequeue a character from queue
		# Compare, if not equal palindrome asumption fails, else continue till last
		if obj.pop_character() != obj.dequeue_character():
			is_palindrome = False
			break
	# Finally print whether string s is palindrome or not.
	# using string format to encode a variable inside a string
	if is_palindrome == True:
		print(f"The word, {s}, is a palindrome.")
	else:
		print(f"The word, {s}, is not a palindrome.")