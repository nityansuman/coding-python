
def find_captains_room(rooms, size):
	"""Method to find the captain's room.

	Args:
		rooms (list): List of all rooms.
		size (int): Size of the group.
	"""
	all_guests = list(map(int, rooms))
	unique_guests = set(all_guests)
	sum_all_guests = sum(all_guests)

	# Get the sum of all the unique room numbers
	sum_unique_guests = sum(unique_guests)

	# Get the difference, in the sum: the captains room will cause this difference
	temp = (sum_unique_guests * size) - sum_all_guests

	# Compute the captain's room number
	return temp // (size - 1)


if __name__ == "__main__":
	# Read input size from stdin
	size = int(input().strip())

	# Read room number list from stdin
	rooms = input().strip().split(" ")

	# Find captain's room
	captains_room_number = find_captains_room(rooms, size)

	print(captains_room_number)
