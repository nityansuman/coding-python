"""
Objective
	In this challenge, we're going to learn about the difference between a class and an instance.

Task
	Write a Person class with an instance variable, age, and a constructor that takes an integer, initial_age, as a parameter. The constructor must assign inittial_age to  age after confirming the argument passed as initial_age is not negative; if a negative argument is passed as initia_age, the constructor should set age to 0 and print `Age is not valid, setting age to 0..` In addition, you must write the following instance methods:

	1. year_passes() should increase the age instance variable by 1.
	2. am_i_old() should perform the following conditional actions:
		If age < 13, print `You are young..`
		If age >= 13 and age < 18, print `You are a teenager..`
		Otherwise, print `You are old..`
	Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format
	Input is handled for you by the stub code in the editor.
	The first line contains an integer, t (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.

Constraints
	1 <= T <= 4
	-5 <= age <= 30

Output Format
	Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or  lines (depending on whether or not a valid  was passed to the constructor).

Sample Input
	4
	-1
	10
	16
	18

Sample Output
	Age is not valid, setting age to 0.
	You are young.
	You are young.

	You are young.
	You are a teenager.

	You are a teenager.
	You are old.

	You are old.
	You are old.
"""


class Person:
	def __init__(self, initial_age):
		# Run some checks on initial_age and set memeber variable `age`
		if initial_age < 0:
			self.age = 0
			print("Age is not valid, setting age to 0..")
		else:
			self.age = initial_age
	
	def am_i_old(self):
		# Run some checks and print correct statement to the console based on the current age value
		if self.age < 13:
			print("You are young..")
		elif self.age >= 13 and self.age < 18:
			print("You are a teenager..")
		else:
			print("You are old..")
	
	def year_passes(self):
		# Increment the age of the person
		self.age += 1


if __name__ == "__main__":
	# Input number of test cases
	t = int(input())

	# For each test case input age
	for i in range(0, t):
		age = int(input())
		
		# Initiate Person class
		p = Person(age)  

		# Call method `am_i_old` using the created object to check age
		p.am_i_old()

		# Call `year_passes` method multiple times to change age value
		for j in range(0, 3):
			p.year_passes()
		
		# Call `am_i_old` method to check new age value
		p.am_i_old()

		# Add an empty new line
		print("")