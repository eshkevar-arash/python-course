def max_3(a, b, c):
    """Return the largest value among three numbers.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.
        c (int | float): The third number.

    Returns:
        int | float: The largest value among `a`, `b`, and `c`.

    Examples:
        >>> max_3(10, 5, 8)
        10
        >>> max_3(-3, -1, -5)
        -1
    """
    return max(a, b, c)




print(help(max_3))