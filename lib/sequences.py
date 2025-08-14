def print_fibonacci(length):
    """
    Prints a list containing the Fibonacci sequence up to the given length.
    Examples:
        print_fibonacci(0) -> []
        print_fibonacci(1) -> [0]
        print_fibonacci(5) -> [0, 1, 1, 2, 3]
    """
    if length <= 0:
        print([])
        return

    if length == 1:
        print([0])
        return

    seq = [0, 1]
    for _ in range(2, length):
        seq.append(seq[-1] + seq[-2])

    print(seq)
