if __name__ == "__main__":
    # Read input from stdin
    n, m, k = list(map(int, input().strip().split()))

    # Count beautiful days
    count = 0
    for x in range(n, m+1):
        y = int(str(x)[::-1])

        if (abs(x - y) % k) == 0:
            count += 1

    print("Number of beatiful days:", count)
