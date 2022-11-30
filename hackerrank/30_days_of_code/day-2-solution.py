
def solve(meal_cost, tip_percent, tax_percent):
	# Compute actual tip
	actual_tip = meal_cost * (tip_percent / 100)

	# Compute actual tax
	actual_tax = meal_cost * (tax_percent / 100)

	# Compute total cost
	total_cost = meal_cost + actual_tax + actual_tip

	# Round off total cost
	print(round(total_cost))


if __name__ == "__main__":
	# Read floating meal cost, integer tip rate,
	# integer tax rate and save to a variable
	meal_cost = float(input())
	tip_percent = int(input())
	tax_percent = int(input())

	# Compute total cost using a method
	solve(meal_cost, tip_percent, tax_percent)
