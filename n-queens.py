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

n = 5
solutions = 0
grid = []
cols_used = set()
up_diags_used = set() # Used to track placed queen's (row + col) diagnonals.
down_diags_used = set() # Used to track placed queen's (row - col) diagnonals.

def print_grid(s, n):
    print("Solution:", s)
    for row in grid:
        print("+---" * n + "+")
        for cell in row:
            print('|', cell, end=" ")
        print('|')
    print("+---" * n + "+")
    return


def check_unique(position, n):
    return True

def solve(row, n):
    global grid
    global solutions

    if row == n:
        position = 0
        if check_unique(position, n):
            solutions += 1
            print_grid(solutions, n)
        return

    for col in range(0, n):
        if col in cols_used or (row + col) in up_diags_used or (row - col) in down_diags_used:
            continue

        cols_used.add(col)
        up_diags_used.add(row + col)
        down_diags_used.add(row - col)
        grid[row][col] = 'Q'

        # Solve the next row by calling ourself recursively.
        solve(row + 1, n)

        # Now backtrack to find more solutions.
        cols_used.remove(col)
        up_diags_used.remove(row + col)
        down_diags_used.remove(row - col)
        grid[row][col] = ' '

    return


def main():
    global grid
    global n

    # Check for any command line args.
    parser = argparse.ArgumentParser(description='This program computes the solutions to the n-queens problem.  That is, how to place n-queens on a chessboard, so they cannot take each other.')
    parser.add_argument('-n', '--size', help='size of board', type=int, default=8)
    parser.add_argument('-a', '--all', help='compute/print non-unique solutions', action='store_true')
    args = parser.parse_args()

    #print(vars(args))

    n = args.size
    all_sols = args.all

    # Show the board size that will be used.
    if all_sols:
        print(f'Finding all solutions using a {n} x {n} board...\n')
    else:
        print(f'Finding unique solutions using a {n} x {n} board...\n')

    # Define an empty grid of the given size.
    grid = [[' '] * n for i in range(0, n)]

    # Take note of the start time and begin.
    start_time = time.time()
    solve(0, n)

    # Print the run-time.
    seconds = time.time() - start_time
    print('Duration:', time.strftime("%H:%M:%S", time.gmtime(seconds)), '\n')

if __name__ == '__main__':
    main()
