"""
You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

The first line contains two integers, N and M separated by a single space,
where N represents the number of people and M represents the number of topics.
N lines follows. Each line contains a binary string of length M.
If the ith line's jth character is 1, then the ith person knows the jth topic;
otherwise, he doesn't know the topic.

2 <= N <= 500
1 <= M <= 500

On the first line, print the maximum number of topics a 2-person team can know.
On the second line, print the number of 2-person teams that can know the maximum number of topics.
"""

if __name__ == "__main__":
    N, M = list(map(int, input().strip().split()))
    T = [int(input(), 2) for _ in range(N)]

    max_topics, num_teams = 0, 0

    for i in range(len(T) - 1):
        for j in range(i + 1, len(T)):
            topics = bin(T[i] | T[j]).count("1")

            if(topics == max_topics):
                num_teams += 1
            if(topics > max_topics):
                max_topics = topics
                num_teams = 1

    print(max_topics, num_teams)
