# Import packages
from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
	def __init__(self, title, author):
		self.title = title
		self.author = author

	@abstractmethod
	def display():
		# Abstract methods are to be implemented in sub-class
		pass


# Create sub-class by inheriting the above parent class
class MyBook(Book):
	def __init__(self, title, author, price):
		self.price = price
		super(MyBook, self).__init__(title, author)

	def display(self):
		print("Title:", self.title)
		print("Author:", self.author)
		print("Price:", self.price)


if __name__ == "__main__":
	# Read input title from stdin
	title = input()

	# Read input author from stdin
	author = input()

	# Read input price from stdin
	price = int(input())

	# Create an instance of the custom class `MyBook`
	new_novel = MyBook(title,author,price)

	# Call `display` class method to print details of the book
	new_novel.display()
