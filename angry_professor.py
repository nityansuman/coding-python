"""
A Discrete Mathematics professor has a class of n students.
Frustrated with their lack of discipline, he decides to cancel class
if fewer than k students are present when class starts.
Given the arrival time of each student, determine if the class is canceled.

The first line of input contains,the number of t test classes/cases.

Each test case consists of two lines.
The first line has two space-separated integers, n(students in the class)
and k(the cancelation threshold).
The second line contains n space-separated integers (a1,a2,..)
describing the arrival times for each student.

If ax<=0 then reached on or before time to class,
else they are late by ax minutes

For each test class,
print the word YES if the class is canceled or NO if it is not.
"""

if __name__ == "__main__":
	T = int(input().strip())
	for x in range(T):
		N, K = input().strip().split(" ")
		N, K = [int(N),int(K)]

		arrival = map(int, input().strip().split(" "))
		arrival = sorted(arrival, key=int)

		print("NO") if arrival[K-1] <= 0 else print("YES")
