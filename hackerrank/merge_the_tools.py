def create_sequences(sequence, factor):
	# Compute sequence and new sequence length
	seq_len = len(sequence)

	# Iteratively create new sequences
	for i in range(0, seq_len, factor):
		# Unique character set placeholder
		seen = set()
		for char in sequence[i:i+factor]:
			if char not in seen:
				# If not seen, print
				seen.add(char)
				print(char, end="")
			else:
				# If seen, ignore
				continue
		# Add newline for next sequence
		print()


if __name__ == "__main__":
	# Read sequenc string from stdin
	sequence = input().strip()

	# Read factor integer from stdin
	factor = int(input().strip())

	# Print new sequences on newlines
	create_sequences(sequence, factor)
