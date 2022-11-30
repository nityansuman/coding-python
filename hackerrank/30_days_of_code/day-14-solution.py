
class Difference:
	def __init__(self, a):
		self.__elements = a

	def comput_diff(self):
		# Identify min and max in the list
		max_element = max(self.__elements)
		min_element = min(self.__elements)

		#  Comput absolute difference
		self.max_diff = abs(max_element - min_element)


if __name__ == "__main__":
	# Read input from stdin in a list
	_ = input()
	a = list(map(int, input().strip().split()))

	# Create an instance of the `Difference` class
	obj = Difference(a)

	# Call class method `comput_diff`
	# The method computes absolute difference between `min` and `max` element of the input
	obj.comput_diff()

	# Access the class memeber variable `max_diff` and print the result
	print(obj.max_diff)
