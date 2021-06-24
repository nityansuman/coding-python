"""
You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.

The first line contains an integer N.
N is the total number of integers in the list.

The second line contains the space separated list of N integers

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False
"""

if __name__ == "__main__":
    N = int(input().strip())
    NUMBER = input().strip().split(" ")

    if all(int(x) >= 0 for x in NUMBER) and any(x == x[::-1] for x in NUMBER):
        print(True)
    else:
        print(False)
