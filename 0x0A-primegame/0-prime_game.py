#!/usr/bin/python3
"""Maria and Ben are playing 0 prime game"""


def isWinner(x, nums):
    """x - no. of rounds
    nums - list of numbers
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    u = [1 for x in range(sorted(nums)[-1] + 1)]
    u[0], u[1] = 0, 0
    for i in range(2, len(u)):
        rm_multiples(u, i)

    for i in nums:
        if sum(u[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiples
    of prime nos.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
