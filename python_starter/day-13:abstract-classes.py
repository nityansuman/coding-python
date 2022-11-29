"""
Objective
	Today, we're taking what we learned yesterday about Inheritance and extending it to Abstract Classes. Because this is a very specific Object-Oriented concept, submissions are limited to the few languages that use this construct.

Task
	Given a Book class and a Solution class, write a MyBook class that does the following:

	- Inherits from Book
	- Has a parameterized constructor taking these 3 parameters:
		- string title
		- string author
		- int price

	- Implements the Book class' abstract display() method so it prints these 3 lines:
		- Title:, a space, and then the current instance's title.
		- Author:, a space, and then the current instance's author.
		- Price:, a space, and then the current instance's price.
	Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring MyBook or your code will not execute.

Input Format
	You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object.

Output Format
	The void display() method should print and label the respective title, author, and price of the MyBook object's instance (with each value on its own line) like so:

	Title: $title
	Author: $author
	Price: $price

	Note: The $ is prepended to variable names to indicate they are placeholders for variables. No need to add when outputing real value.

Sample Input
	The following input from stdin is handled by the locked stub code in your editor:

	The Alchemist
	Paulo Coelho
	248

Sample Output
	The following output is printed by your display() method:

	Title: The Alchemist
	Author: Paulo Coelho
	Price: 248
"""


# Import abstract package
from abc import ABCMeta, abstractmethod

# Base class
class Book(object, metaclass=ABCMeta):
	# Abstract class constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author

	# Abstract method
    @abstractmethod
    def display(): pass


# MyBook class
class MyBook(Book):
	# Sub-class Constructor
	def __init__(self, title, author, price):
		self.price = price
		# Initiate base class
		super(MyBook, self).__init__(title, author)

	# Implement the abstract method
	def display(self):
		print("Title:", self.title)
		print("Author:", self.author)
		print("Price:", self.price)


# Entry point of the program
if __name__ == "__main__":
	# Read input
	title = input()
	author = input()
	price = int(input())

	# Create MyBook object
	new_novel = MyBook(title, author, price)

	# Call display() method of the object
	# Method returns none (void)
	new_novel.display()