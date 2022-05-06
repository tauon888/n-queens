#-------------------------------------------------------------------------------
#      Name:  queens.py
#   Purpose:  Use backtracking to find all 8-queens solutions.
#
#    Author:  Mike Smith (Based on Thorstem's Suduko implementation)
#
#   Created:  02/05/2022
# Copyright:  (c) Mike 2022
#   Licence:  <your licence>
# Reference:  https://en.wikipedia.org/wiki/Eight_queens_puzzle
#   Results:  Gridsize  Solutions     Tested
#                  4            2       Y
#                  5           10       Y
#                  6            4       Y
#                  7           40       Y
#                  8           92       Y
#                  9          352       Y
#                 10          724       Y
#                 11         2680       Y
#                 12        14200       Y
#-------------------------------------------------------------------------------

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

gridsize = 12
solutions = 0


def print_grid(s):
    print("Solution:", s)
    for row in grid:
        for cell in row:
            print('|', cell, end=" ")
        print('|')
    return


def possible(row, col):
    global grid
    global gridsize
    # Test for any same column conflict.
    for c in range(0, gridsize):
        if grid[row][c] == 'Q':
            #print("T1")
            return False
    # Test for any same row conflict.
    for r in range(0, gridsize):
        if grid[r][col] == 'Q':
            #print("T2")
            return False

    # Test for any diagonal conflicts.

    # Leading (\) diagonal test.
    if row == col:
        for r in range(0, gridsize):
            if grid[r][r] == 'Q':
                #print("T3")
                return False
    elif row > col:
        start_row = row - col
        for r, c in zip(range(start_row, gridsize), range(0, gridsize - start_row)):
            if grid[r][c] == 'Q':
                #print("T4")
                return False
    else:
        start_col = col - row
        for r, c in zip(range(0, gridsize - start_col), range(start_col, gridsize)):
            if grid[r][c] == 'Q':
                #print("T5")
                return False

    # Trailing (/) diagonal test.
    sum = row + col
    terms = 0
    start_row = 0
    stop_row = 0
    if sum <= gridsize - 1:
        terms = sum + 1
        start_row = 0
        stop_row = sum + 1
    else:
        terms = (2 * gridsize) - 1 - sum
        start_row = sum - (gridsize - 1)
        stop_row = gridsize - 1

    for r in range(start_row, stop_row):
        if grid[r][sum-r] == 'Q':
                #print("T6")
                return False

    return True


def solve(row):
    global grid
    global solutions
    #print(f" Row-{row}")
    placed = False
    for col in range(0, gridsize):
        if grid[row][col] == ' ':
            if possible(row, col):
                grid[row][col] = 'Q'
                placed = True
                #print_grid()
                #input("Cont?")
                if row == gridsize - 1:
                    solutions += 1
                    print_grid(solutions)
                    #input("More?")
                    grid[row][col] = ' '
                else:
                    #print("Calling solve...")
                    solve(row + 1)
                    grid[row][col] = ' '
    if not placed:
        pass
        #print("Backtracking...")

    #print("Solve returning...")
    return


def main():
    solve(0)
    #print(possible(0,0))
    #print(possible(1,2))
    #print(possible(2,4))

if __name__ == '__main__':
    main()
