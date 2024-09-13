#!/usr/bin/python3
"""solving the N-Queens conundrum"""
import sys


def is_safe(board, row, col):
    """Check if the position is safe for the queen
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Backtrack to find all solutions
    """
    if row == N:
        # Format the solution in the required format
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def main():
    """Main function to handle input validation
    and trigger the solution search
    """
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

    # Initialize the board and solutions list
    board = [-1] * N
    solutions = []

    # Start solving from the first row
    solve_nqueens(N, 0, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
