#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col] == 1:
            return False
        if (col - (row - i)) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if (col + (row - i)) < len(board) and board[i][col + (row - i)] == 1:
            return False
    return True


def solve_nqueens(board, row):
    """Recursively solve the N queens problem using backtracking."""
    if row >= len(board):
        print_board(board)
        return
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0


def print_board(board):
    """Print the board configuration as a list of positions."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def main():
    """Main function to handle input and initiate the solution process."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
