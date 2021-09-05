def utopian_tree(n):
    # Initial height of the tree
    height = 1

    # First season as summer
    is_summer = True

    if n == 0:
        return height

    while n > 0:
        if is_summer:
            height *= 2
            is_summer = False
            n -= 1
        if not is_summer and n > 0:
            height += 1
            is_summer = True
            n -= 1

    return height


if __name__ == "__main__":
    # Read integer input denoting test cases from stdin
    t = int(input().strip())

    # For each test case
    for x in range(t):

        # Read integer input denoting cycles from stdin
        n = int(input().strip())

        # Compute utopian tree height after n cycles
        print("Height of the `Utopian` tree:", utopian_tree(n))
