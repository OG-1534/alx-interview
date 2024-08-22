#!/usr/bin/python3
"""Module for making change"""


def makeChange(coins, total):
    """Function for clasic Bottom-Up dynamic programming"""
    tempo_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            tempo_value += total // coin
            total = total % coin

    return tempo_value if total == 0 else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
