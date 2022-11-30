def wrap(string: str, max_width: int) -> str:
	tmp = ""
	for i in range(len(string)):
		if i % max_width == 0 and i != 0:
			tmp += "\n"
			tmp += string[i]
		else:
			tmp += string[i]
	return tmp


if __name__ == "__main__":
	input_string = input().strip()
	width = int(input().strip())

	print(wrap(input_string, width))
