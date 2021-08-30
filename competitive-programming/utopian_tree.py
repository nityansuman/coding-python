def utopian_tree(n: int) -> int:
    """Method to compute height of the utopian tree after `n` cycles of growth.

	Utopian tree doubles it's height every summer and grows by 1 unit every spring
	i.e., every year the tree goes through two cycles of growth.

    Args:
		n (int): Number of growth cycles.

    Returns:
		int: Height of the tree after `n` cycles.
    """
    height = 1 # Initial height of the tree
    is_summer = True # First season as `summer`

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
