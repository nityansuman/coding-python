"""
Given an array of n integers, return an array of all the unique paris [nums[a], nums[b]] such that:
0 <= a, b < n where a and b are distinct and nums[a] + nums[b] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,2],[0,0],[-1,1]]
"""

def two_sum(arr, target):
	mlist = list()
	seen = dict()

	for a in arr:
		if target - a in seen:
			mlist.append((seen[target - a], a))

		seen[a] = a

	return mlist


if __name__ == "__main__":
	arr = list(map(int, input().strip().split()))
	target = int(input().strip())

	print(two_sum(arr, target))
