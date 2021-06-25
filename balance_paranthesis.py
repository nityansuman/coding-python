"""
Given a string of paranthesis check if it is balanced or not.

For every opening of a paranthesis one needs to have a closing paranthesis for it
to be considered as balanced.

Ex: (())() is balanced
"""

if __name__ == "__main__":
	STRING = input().strip()
	SYMBOL = list(STRING)
	count = 0

	for sym in SYMBOL:
		if sym == "(":
			count += 1
		else:
			count -= 1

	if count == 0:
		print("Balanced")
	else:
		print("Un-balanced")
