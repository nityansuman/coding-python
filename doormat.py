"""
Design a door mat.
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:
Mat size must be N X M. (N is an odd natural number and M is 3 times N.)
The design should have "WELCOME" written in the center.
The design pattern should only use "|" and "." and "-" characters.

Size: 11 x 33
	---------------.|.---------------
	------------.|..|..|.------------
	---------.|..|..|..|..|.---------
	------.|..|..|..|..|..|..|.------
	---.|..|..|..|..|..|..|..|..|.---
	-------------WELCOME-------------
	---.|..|..|..|..|..|..|..|..|.---
	------.|..|..|..|..|..|..|.------
	---------.|..|..|..|..|.---------
	------------.|..|..|.------------
	---------------.|.---------------

Size: N = 7 and M = 21
	---------.|.---------
	------.|..|..|.------
	---.|..|..|..|..|.---
	-------WELCOME-------
	---.|..|..|..|..|.---
	------.|..|..|.------
	---------.|.---------

Input
A single line containing the space separated values of N and M.
Output the design pattern.
"""

if __name__ == "__main__":
	N, M = input().strip().split(" ")
	N, M = [int(N), int(M)]

	for i in range(1, N, 2):
		print("-" * ((M - i * 3) // 2) + ("|".center(3, "."))
			  * i + "-" * ((M - i * 3) // 2))

	print("WELCOME".center(M, "-"))

	for i in range(N - 2, -1, -2):
		print("-" * ((M - i * 3) // 2) + ("|".center(3, "."))
			  * i + "-" * ((M - i * 3) // 2))
