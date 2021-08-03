if __name__ == "__main__":
    # Read number of test cases input from stdin
    T = int(input().strip())

    X = 3 # Counter start

    # Placeholder variables
    total, diff, n = 0, 0, 0

    # Compute counter
    while T > total:
        diff = (X * 2**(n+1)) - (X * 2**n)
        total += diff
        n += 1

    print(total - T + 1)
