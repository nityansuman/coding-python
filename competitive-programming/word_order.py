# Import packages
from collections import OrderedDict


if __name__ == "__main__":
	# Read number of word input integer from stdin
	num_words = int(input().strip())

	# Words mapping placeholder
	mapping = OrderedDict()

	for i in range(num_words):
		# Read word from stdin
		word = input().strip()

		# Create mapping of the word
		if word not in mapping:
			mapping[word] = 1
		else:
			mapping[word] += 1

	# Distinct words and their frequencies
	num_unique_words, word_frequencies = len(mapping.keys()), list(mapping.values())

	# Output on newlines in appropriate format
	print(num_unique_words)

	for f in word_frequencies:
		print(f, end=" ")
