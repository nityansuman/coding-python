# Import packages
from collections import OrderedDict

if __name__ == "__main__":
	num_words = int(input().strip())

	mapping = OrderedDict()
	count = 0

	for i in range(num_words):
		word = input().strip()

		if word not in mapping:
			mapping[word] = 1
			count += 1
		else:
			mapping[word] += 1

	num_unique_words, word_frequencies = count, list(mapping.values())

	print(num_unique_words)

	for f in word_frequencies:
		print(f, end=" ")
