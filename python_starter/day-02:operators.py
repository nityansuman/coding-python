"""
Objective
	In this challenge, you'll work with arithmetic operators.

Task
	Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format
	There are 3 lines of numeric input:
	The first line has a double, `meal_cost` (the cost of the meal before tax and tip).
	The second line has an integer, `tip_percent` (the percentage of `meal_cost` being added as tip).
	The third line has an integer, `tax_percent` (the percentage of `meal_cost` being added as tax).

Output Format
	Print the total meal cost, where `total_cost` is the rounded integer result of the entire bill (`meal_cost` with added tax and tip).

Sample Input
	12.00
	20
	8

Sample Output
	15
"""


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
	actual_tip = meal_cost * (tip_percent / 100)
	actual_tax = meal_cost * (tax_percent / 100)
	total_cost = meal_cost + actual_tax + actual_tip
	print(round(total_cost))


if __name__ == "__main__":
	# Read input and convert string to type cast
	meal_cost = float(input())
	tip_percent = int(input())
	tax_percent = int(input())

	# Calculate total cost
	solve(meal_cost, tip_percent, tax_percent)