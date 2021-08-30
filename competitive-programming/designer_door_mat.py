if __name__ == "__main__":
    # Read input from stdin
    N, M = input().strip().split(" ")
    N, M = [int(N), int(M)]

    # Draw top half
    for i in range(1, N, 2):
        print("-" * ((M - i * 3) // 2) + ("|".center(3, "."))
                  * i + "-" * ((M - i * 3) // 2))

    # Print message
    print("WELCOME".center(M, "-"))

    # Draw bottom half
    for i in range(N - 2, -1, -2):
        print("-" * ((M - i * 3) // 2) + ("|".center(3, "."))
                  * i + "-" * ((M - i * 3) // 2))
