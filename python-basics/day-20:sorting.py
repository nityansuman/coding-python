"""
Objective
	Today, we're discussing a simple sorting algorithm called `Bubble Sort`.
	Bubble sort has a worst-case and average complexity of О(n2), where n is the number of items being sorted. Most practical sorting algorithms have substantially better worst-case or average complexity, often O(n log n). Even other О(n2) sorting algorithms, such as insertion sort, generally run faster than bubble sort, and are no more complex. Therefore, bubble sort is not a practical sorting algorithm.

Task
	Given an array, A, of size N distinct elements, sort the array in ascending order using the Bubble Sort algorithm.
	Once sorted, print the following  lines:
		Array is sorted in num_swaps swaps.
			where num_swaps is the number of swaps that took place.
		First Element: first_element
			where first_element is the first element in the sorted array.
		Last Element: last_element
			where last_element is the last element in the sorted array.

Input Format
	The first line contains an integer, N, denoting the number of elements in array A.
	The second line contains N space-separated integers describing the respective values of A.

Constraints
	2 <= N <= 600
	1 <= Ai <= 10e6, where 0 <= i < N.

Output Format
	Print the following three lines of output:
	Array is sorted in num_swaps swaps.
	First Element: first_element
	Last Element: last_element

Sample Input 0
	3
	1 2 3

Sample Output 0
	Array is sorted in 0 swaps.
	First Element: 1
	Last Element: 3

Sample Input 1
	3
	3 2 1

Sample Output 1
	Array is sorted in 3 swaps.
	First Element: 1
	Last Element: 3
"""


# Modified Bubble Sort algorithm to return sorted array along with number of swaps
def bubble_sort(array):
	num_swaps = 0
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			# Sorting in ascending order
			if array[j] < array[i]:
				# Swap
				array[i], array[j] = array[j], array[i]
				num_swaps += 1
			else:
				continue
	return num_swaps, array


# Entry point of the program
if __name__ == "__main__":
	# Read input ineteger denoting N
	N = int(input().strip())

	# Read Array
	A = list(map(int, input().strip().split(" ")))

	# Perform bubble sort
	num_swaps, A = bubble_sort(A)
	print(f"Array is sorted in {num_swaps} swaps.")
	print(f"First Element: {A[0]}")
	print(f"Last Element: {A[-1]}")