"""
Objective
	Today, we're delving into Inheritance.

Task
	Write two classes, Person and Student, where Person is the base class and Student is the derived class.
	Student should inherit all the properties of Person.

	Parent class should have an info() method that prints sttudent information (first_name, last_name and id_num).
	Student should have a calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
		Letter | Average
			O : 90 <= a <= 100
			E : 80 <= a < 90
			A : 70 <= a < 80
			P : 55 <= a < 70
			D : 40 <= a < 55
			T : a < 40

Input Format
	The first line contains first_name, last_name, and id_num, respectively.
	The second line contains the number of test scores.
	The third line of space-separated integers describes scores.

Constraints
	a <= [first_name, last_name] <= 10
	|id_num| = 7
	0 <= [score, average] <= 100

Output Format
	First line of output first_name and last_name separated by a comma.
	Second line of output, student id_num..
	Third line of output, print grade achieved.

Sample Input
	Heraldo Memelli 8135627
	2
	100 80

Sample Output
	Name: Memelli, Heraldo
	ID: 8135627
	Grade: O
"""


# Base class / Parent class
class Person:
	def __init__(self, first_name, last_name, id_num):
		# Class constructor
		self.first_name = first_name
		self.last_name = last_name
		self.id_num = id_num
	
	def info(self):
		# Method to print student information
		print("Name:", self.last_name + ",", self.first_name)
		print("ID:", self.id_num)


# Derived class / Child class: Class inheriting `Parent` class
class Student(Person):
	def __init__(self, first_name, last_name, id_num, scores):
		# Class constructor
		self.scores = scores
		# Initiating parent class
		super(Student, self).__init__(first_name, last_name, id_num)
	
	def calculate(self):
		# Method to compute grade based out of average score
		average_score = sum(self.scores) / len(self.scores)
		if average_score >= 90 and average_score <= 100:
			return "O"
		elif average_score >= 80 and average_score < 90:
			return "E"
		elif average_score >= 70 and average_score < 80:
			return "A"
		elif average_score >= 55 and average_score < 70:
			return "P"
		elif average_score >= 40 and average_score < 55:
			return "D"
		else:
			return "T"


if __name__ == "__main__":
	# Read first line of input
	line = input().split()
	first_name = line[0]
	last_name = line[1]
	id_num = line[2]
	
	# Read number of test scores
	numScores = int(input())

	# Read test scores separated by single spaces
	scores = list(map(int, input().split()))

	# Create a `Student` object
	s = Student(first_name, last_name, id_num, scores)

	# Print information: full name and identification number
	s.info()

	# Calculate grade
	print("Grade:", s.calculate())