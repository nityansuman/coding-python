# Import packages
from typing import List


def acm_team(topic: List[str]) -> List[int]:
    """[summary]

    Args:
        topic (List[str]): [description]

    Returns:
        List[int, int]: [description]
    """
    # Convert string to binary
    topic = [int(t, 2) for t in topic]

    max_topics, num_teams = 0, 0

    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            topics = bin(topic[i] | topic[j]).count("1")

            if(topics == max_topics):
                num_teams += 1

            if(topics > max_topics):
                max_topics = topics
                num_teams = 1

    return [max_topics, num_teams]


if __name__ == "__main__":
    # Read input from stdin
    n, m = list(map(int, input().strip().split()))

    # Read topic input from stdin
    topic = list()
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    print("Result:", acm_team(topic))
