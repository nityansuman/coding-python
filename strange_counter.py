"""
Bob has a strange counter. At the first second, t=1, it displays the number 3.
At each subsequent second, the number displayed by the counter decrements by 1.
The counter counts down in cycles. In the second after the counter counts down
to 1, the number becomes 2 times the initial number for that countdown cycle
and then continues counting down from the new initial number in a new cycle.

First cycle
1->3
2->2
3->1
Second cycle
4->6
5->5
6->4
7->3
8->2
9->1 and so on...

Given a time t, find and print the value displayed by the counter at time t.
"""

if __name__ == "__main__":
	T = int(input().strip())
	X = 3
	TOTAL, DIFF, N = 0, 0, 0

	while T > TOTAL:
		DIFF = (X * 2**(N+1)) - (X * 2**N)
		TOTAL += DIFF
		N += 1

	print(TOTAL - T + 1)
