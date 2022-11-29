"""
Objective
	Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure.

Task
	Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber.
	If an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format
	The first line contains an integer, n, denoting the number of entries in the phone book.
	Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.

	After the n lines of phone book entries, there are an `unknown number` of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Constraints
	1 <= n <= 10e5
	1 <= queries <= 10e5

Output Format
	On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phone number in the format name=phoneNumber.

Sample Input
	3
	sam 99912222
	tom 11122222
	harry 12299933
	sam
	edward
	nityan
	kumar

Sample Output
	sam=99912222
	Not found
	harry=12299933
	Not found
	Not found
"""

# Import package
from sys import stdin


if __name__ == "__main__":
    # Read number of entries
    n = int(input())

    # Create an empty dictionary/mapping
    teleophone_directory = dict()
    
    # Read name and phone number entries
    for i in range(n):
        name, phone_number = input().strip().split()
        teleophone_directory[name] = phone_number
    
    # Read unknown number of search query
	# Use stdin to read all input at once and split newlines to create a list
    search_names = stdin.read().strip().split()
	# For each search name
    for search_name in search_names:
		# Find name else prompt appropriate message
        if search_name in teleophone_directory.keys():
            print(f"{search_name}={teleophone_directory[search_name]}")
        else:
            print("Not found")