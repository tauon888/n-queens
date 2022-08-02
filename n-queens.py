#-------------------------------------------------------------------------------
#      Name:  n-queens.py
#   Purpose:  Use backtracking to find all 8-queens solutions.
#             Can show unique (default) and non-unique solutions (-a switch).
#
#    Author:  Mike Smith (Based on Thorsten Altenkirch's Suduko implementation)
#
#   Created:  02/05/2022
# Copyright:  (c) Mike 2022
# Reference:  https://en.wikipedia.org/wiki/Eight_queens_puzzle
#-------------------------------------------------------------------------------
import time
import argparse

solutions = 0
board = []
cols_used = set()
up_diags_used = set() # Used to track placed queen's (row + col) diagnonals.
down_diags_used = set() # Used to track placed queen's (row - col) diagnonals.

def print_board(s, n):
    print("Solution:", s)
    for queen in board:
        print("+---" * n + "+")
        for col in range(0, n):
            if col == queen:
                print('|', 'Q', end=" ")
            else:
                print('|', ' ', end=" ")
        print('|')
    print("+---" * n + "+")
    print()


def check_unique(position, n):
    return True


def solve(row, n, unique):
    global board
    global solutions

    if row == n:
        position = 0
        if unique and check_unique(position, n):
            solutions += 1
            print_board(solutions, n)
        else:
            solutions += 1
            print_board(solutions, n)
        return

    for col in range(0, n):
        if col in cols_used or (row + col) in up_diags_used or (row - col) in down_diags_used:
            continue

        cols_used.add(col)
        up_diags_used.add(row + col)
        down_diags_used.add(row - col)
        board[row] = col

        # Solve the next row by calling ourself recursively.
        solve(row + 1, n, unique)

        # Now backtrack to find more solutions.
        cols_used.remove(col)
        up_diags_used.remove(row + col)
        down_diags_used.remove(row - col)
        board[row] = 0


def main():
    global board

    # Check for any command line args.
    parser = argparse.ArgumentParser(description='This program computes the solutions to the n-queens problem.  That is, how to place n-queens on a chessboard, so they cannot take each other.')
    parser.add_argument('-n', '--size', help='size of board', type=int, default=8)
    parser.add_argument('-a', '--all', help='compute/print non-unique solutions', action='store_true')
    args = parser.parse_args()

    #print(vars(args))

    n = args.size
    unique = not args.all
    version = 'V1.0'
    print('N-Queens Solver {}'.format(version))

    # Show the board size that will be used.
    if unique:
        print(f'Finding unique solutions using a {n}x{n} board...\n')
    else:
        print(f'Finding all (non-unique) solutions using a {n}x{n} board...\n')

    # Define an empty grid of the given size.
    #grid = [[' '] * n for i in range(0, n)]
    board = [0 for i in range(0, n)]

    # Take note of the start time and begin.
    start_time = time.time()
    solve(0, n, unique)

    # Print the run-time.
    seconds = time.time() - start_time
    print('Duration:', time.strftime("%H:%M:%S", time.gmtime(seconds)), '\n')

if __name__ == '__main__':
    main()
