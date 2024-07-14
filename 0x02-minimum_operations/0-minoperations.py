#!/usr/bin/python3

""" Module for Minimum operations """


def minOperations(n):
    """
    In a text file, there is 1 char H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operations, iterator = 0, 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
