def create_sequences(sequence, factor):
	seq_len = len(sequence)

	for i in range(0, seq_len, factor):
		seen = set()
		for char in sequence[i:i+factor]:
			if char not in seen:
				seen.add(char)
				print(char, end="")
			else:
				continue
		print()


if __name__ == "__main__":
	sequence = input().strip()
	factor = int(input().strip())

	create_sequences(sequence, factor)
