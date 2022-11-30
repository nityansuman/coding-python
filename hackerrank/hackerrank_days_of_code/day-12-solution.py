
# Parent class
class Person:

	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


# Child class inherits parent class
class Student(Person):

	def __init__(self, firstName, lastName, idNum, scores):
		super(Student, self).__init__(firstName, lastName, idNum)
		self.scores = scores

	def calculate(self):
		# Compute mean score
		average_score = sum(self.scores) / len(self.scores)

		# Assign grades according to the set rule
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
	# Read input linear from stdin
	line = input().split()

	# Get student details
	firstName = line[0]
	lastName = line[1]
	idNum = line[2]

	# Read number of score integer from stdin
	numScores = int(input())

	# Read scores integer from stdin
	scores = list(map(int, input().split()))

	# Instantiat Student class
	student_object = Student(firstName, lastName, idNum, scores)

	# Call member method to print details
	student_object.printPerson()

	# Call member method to compute grade and print
	print("Grade:", student_object.calculate())
