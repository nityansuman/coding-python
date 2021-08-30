"""
Objective
	Today we're discussing scope.

	The absolute difference between two integers, a and b, is written as |a-b|.
	The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in elements.
	The Difference class is started for you in the editor. It has a private integer array (elements) for storing N non-negative integers, and a public integer (maximum_difference) for storing the maximum absolute difference.

Task
	Write the Difference class:
		- A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
		- A compute_difference method that finds the `maximum absolute difference` between `any` 2 numbers in N and stores it in the elements instance variable.

Input Format
	You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in  lines of input; the first line contains , and the second line describes the  array.

Constraints
	1 <= N <= 10
	1 < elements[i] <= 100, where 0 <= 1 <= N -1

Output Format
	You are not responsible for printing any output; the Solution class will print the value of the maximum_difference instance variable.

Sample Input
	3
	1 2 5

Sample Output
	4
"""


# Base class
class Difference:
	# Class constructor
	def __init__(self, e):
		self.__elements = a

	# Your code here
	def compute_difference(self):
		# One-shot logic - solution when N is very large
		max_element = max(self.__elements)
		min_element = min(self.__elements)
		self.maximum_difference = abs(max_element - min_element)
		# Brute force logic - as N is very small either solution works or some other will work too
		# self.maximum_difference = 0
		# for i in range(0, n):
		# 	for j in range(i+1, n):
		# 		diff = abs(self.__elements[i] - self.__elements[j])
		# 		if diff > self.maximum_difference:
		# 			self.maximum_difference = diff
		# 		else:
		# 			continue


# Entry point of the program
if __name__ == "__main__":
	# Read number of elements
	_ = input()

	# Read all single spaced elements
	a = [int(e) for e in input().split(' ')]

	# Create class instance
	d = Difference(a)

	# Call method on object
	d.compute_difference()

	# Access instance variable to find solution
	print(d.maximum_difference)