#-------------------------------------------------------------------------------
#      Name:  n-queens.py
#   Purpose:  Use backtracking to find all 8-queens solutions.
#
#    Author:  Mike Smith (Based on Thorstem's Suduko implementation)
#
#   Created:  02/05/2022
# Copyright:  (c) Mike 2022
#   Licence:  <your licence>
# Reference:  https://en.wikipedia.org/wiki/Eight_queens_puzzle
#-------------------------------------------------------------------------------
import sys
import time

"""
grid = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
"""

grid_size = 5
solutions = 0
#debug = True
debug = False
grid = []

def print_grid(s):
    print("Solution:", s)
    for row in grid:
        print("+---" * grid_size + "+")
        for cell in row:
            print('|', cell, end=" ")
        print('|')
    print("+---" * grid_size + "+")
    return


def possible(row, col):
    global grid
    global grid_size
    # Test for any same column conflict.
    for c in range(0, grid_size):
        if grid[row][c] == 'Q':
            return False
    # Test for any same row conflict.
    for r in range(0, grid_size):
        if grid[r][col] == 'Q':
            return False

    # Test for any diagonal conflicts.

    # Leading-Down (\) diagonal test.
    if row == col:
        for r in range(0, grid_size):
            if grid[r][r] == 'Q':
                return False
    elif row > col:
        start_row = row - col
        for r, c in zip(range(start_row, grid_size), range(0, grid_size + 1 - start_row)):
            if grid[r][c] == 'Q':
                return False
    else:
        start_col = col - row
        for r, c in zip(range(0, grid_size - start_col), range(start_col, grid_size)):
            if grid[r][c] == 'Q':
                return False

    # Trailing-Up (/) diagonal test.
    sum = row + col
    start_row = 0
    stop_row = 0
    if sum <= grid_size - 1:
        start_row = 0
        stop_row = sum + 1
    else:
        start_row = sum - (grid_size - 1)
        stop_row = grid_size - 1

    for r in range(start_row, stop_row):
        if grid[r][sum-r] == 'Q':
                return False

    return True


def solve(row):
    global grid
    global solutions
    if debug:
        print(f" Row-{row}")
    placed = False
    for col in range(0, grid_size):
        if grid[row][col] == ' ':
            if possible(row, col):
                grid[row][col] = 'Q'
                placed = True
                #print_grid()
                #input("Cont?")
                if row == grid_size - 1:
                    solutions += 1
                    print_grid(solutions)
                    #input("More?")
                    grid[row][col] = ' '
                else:
                    solve(row + 1)
                    grid[row][col] = ' '
    if not placed:
        pass
        if debug:
            print("Backtracking...")

    if debug:
        print("Solve returning...")
    return


def main():
    global grid
    global grid_size
    
    # Check for any command line args.
    num_args = len(sys.argv)
    if num_args < 2:
        while True:
            try:
                grid_size = int(input("Board size, n? "))
                break
            except ValueError:
                print("Please input a number")
                continue            
    elif num_args == 2:
        grid_size = int(sys.argv[1])
    else:
        print("Too many parameters")
        sys.exit(2)
      
    # Show the board size that will be used.
    print(f'Using an {grid_size} x {grid_size} board')

    # Define an empty grid of the given size.
    grid = [[' '] * grid_size for i in range(0, grid_size)]
    #print_grid(21)
    # Take note of the start time and begin.
    start_time = time.time()      
    solve(0)
    
    # Print the run-time.
    seconds = time.time() - start_time
    print('Duration:', time.strftime("%H:%M:%S", time.gmtime(seconds)), '\n')
    #print(possible(0,0))
    #print(possible(1,2))
    #print(possible(2,4))

if __name__ == '__main__':
    main()
