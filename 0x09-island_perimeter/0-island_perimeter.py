#!/usr/bin/python3
"""Module for Island Perimeter
"""


def island_perimeter(grid):
    """
    Compute perimeter of the island described in grid
    Args:
        grid: 2d list of integers, 0(water) or 1(land)
    Return:
        perimeter of the island
    """

    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    x += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    x += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    x += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    x += 1
    return x
