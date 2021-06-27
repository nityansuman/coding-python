# Import packages
import os

#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
	# Convert string to binary
	topic = [int(t, 2) for t in topic]

	# Counter
	max_topics, num_teams = 0, 0

	# Iterate over topic
	for i in range(len(topic) - 1):
		for j in range(i + 1, len(topic)):
			# Count learned topics
			topics = bin(topic[i] | topic[j]).count("1")
			if(topics == max_topics):
				num_teams += 1
			if(topics > max_topics):
				max_topics = topics
				num_teams = 1
	return [max_topics, num_teams]


if __name__ == "__main__":
	# Read input from file
	fptr = open(os.environ["OUTPUT_PATH"], "w")

	# Process input
	first_multiple_input = input().rstrip().split()
	n = int(first_multiple_input[0])
	m = int(first_multiple_input[1])

	# Collection placeholder
	topic = list()

	# Read input from stdin
	for _ in range(n):
		topic_item = input()
		topic.append(topic_item)

	# Execute method to get results
	result = acmTeam(topic)

	# Write to file
	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	# Close file
	fptr.close()
