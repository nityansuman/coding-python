
class Person:
	def __init__(self, initialAge):
		# Set current age
		if initialAge < 0:
			self.age = 0
			print("Age is not valid, setting age to 0.")
		else:
			self.age = initialAge

	def amIOld(self):
		# Print message based on current age
		if self.age < 13:
			print("You are young.")
		elif self.age >= 13 and self.age < 18:
			print("You are a teenager.")
		else:
			print("You are old.")

	def yearPasses(self):
		# Increment age by one
		self.age += 1


if __name__ == "__main__":
	# Read number of test cases and save to a variable
	t = int(input())

	# For each test case
	for i in range(0, t):

		# Read age integer and save to a variable
		age = int(input())

		# Create Person class object using the read age
		p = Person(age)

		# Call class method to get results
		p.amIOld()

		# Call class method thrice to increment age
		for j in range(0, 3):
			p.yearPasses()

		# Call class method to get results
		p.amIOld()
		print("")
