def find_captains_room(rooms, size):
	all_guests = list(map(int, rooms))

	unique_guests = set(all_guests)
	sum_all_guests = sum(all_guests)

	sum_unique_guests = sum(unique_guests)
	temp = (sum_unique_guests * size) - sum_all_guests

	return temp // (size - 1)


if __name__ == "__main__":
	size = int(input().strip())
	rooms = input().strip().split(" ")

	captains_room_number = find_captains_room(rooms, size)
	print(captains_room_number)
