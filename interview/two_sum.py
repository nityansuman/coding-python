"""
Given an array of n integers, return an array of all the unique paris [nums[a], nums[b]] such that:
0 <= a, b < n where a and b are distinct and nums[a] + nums[b] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,2],[0,0],[-1,1]]
"""

def two_sum(arr, target):
    # Placeholder to store all identified pairs
    mlist = list()

    # Placeholder for mapping array elements
    seen = dict()

    # Iterate over the array
    for a in arr:
        # If sum complement present
        if target - a in seen:
            mlist.append((seen[target - a], a))

        # Add current element to mapping
        seen[a] = a

    # Return itdentified pairs
    return mlist


if __name__ == "__main__":
    # Read integer array from stdin
    arr = list(map(int, input().strip().split()))

    # Read target sum from stdin
    target = int(input().strip())

    # Identify appropriate pairs
    result = two_sum(arr, target)
    print(result)
