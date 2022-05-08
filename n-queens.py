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

grid_size = 5
solutions = 0
#debug = True
debug = False
grid = []
cols_used = set()
up_diags_used = set() # (row + col)
down_diags_used = set() # (row - col)

def print_grid(s):
    print("Solution:", s)
    for row in grid:
        print("+---" * grid_size + "+")
        for cell in row:
            print('|', cell, end=" ")
        print('|')
    print("+---" * grid_size + "+")
    return


def solve(row):
    global grid
    global solutions

    if debug:
        print(f" Row-{row}")
        
    if row == grid_size:
        solutions += 1
        print_grid(solutions)
        return        
        
    for col in range(0, grid_size):
        if col in cols_used or (row + col) in up_diags_used or (row - col) in down_diags_used:
            continue
        
        cols_used.add(col)
        up_diags_used.add(row + col)
        down_diags_used.add(row - col)
        grid[row][col] = 'Q'
        
        # Solve the next row by calling ourself recursively.
        solve(row + 1)

        # Now backtrack to find more solutions.
        cols_used.remove(col)
        up_diags_used.remove(row + col)
        down_diags_used.remove(row - col)
        grid[row][col] = ' '
        
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
