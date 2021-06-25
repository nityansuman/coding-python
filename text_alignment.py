"""
In Python, a string of text can be aligned left, right and center.

.ljust(width)
This method returns a left aligned string of length width.
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------

.center(width)
This method returns a centered string of length width.
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

.rjust(width)
This method returns a right aligned string of length width.
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

Print the symbol of hackerrank using a set symbol in 2D

	H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
					HHHHHHHHH
					 HHHHHHH
					  HHHHH
					   HHH
						H
"""

if __name__ == "__main__":
	# Thickness must be an odd number
	THISKNESS = int(input())
	S = "H"

	# Top cone
	for i in range(THISKNESS):
		print((S * i).rjust(THISKNESS - 1) + S + (S * i).ljust(THISKNESS - 1))

	# Top pillars
	for i in range(THISKNESS + 1):
		print((S * THISKNESS).center(THISKNESS * 2) +
			  (S * THISKNESS).center(THISKNESS * 6))

	# Middle belt
	for i in range((THISKNESS + 1) // 2):
		print((S * THISKNESS * 5).center(THISKNESS * 6))

	# Bottom pillars
	for i in range(THISKNESS + 1):
		print((S * THISKNESS).center(THISKNESS * 2) +
			  (S * THISKNESS).center(THISKNESS * 6))

	# Bottom cone
	for i in range(THISKNESS):
		print(((S * (THISKNESS - i - 1)).rjust(THISKNESS) + S
			   + (S * (THISKNESS - i - 1)).ljust(THISKNESS)).rjust(THISKNESS * 6))
