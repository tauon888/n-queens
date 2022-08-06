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

debug = False
debug_args = []
sol_count = 0
solutions = []
cols_used = set()
up_diags_used = set() # Used to track placed queen's (row + col) diagnonals.
down_diags_used = set() # Used to track placed queen's (row - col) diagnonals.

def print_board(board, sol_count, n, count_only):
    print("Solution:", sol_count)
    if not count_only:
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


def summarize(board):
    # This function returns a flattened string showing the board position.
    return ' '.join(str(x) for x in board)


def rotate_90(board, n):
    # This function returns a 90 degree anti-clockwise rotation of the given board position.
    rotated_board = [0 for i in range(0, n)]
    for row in range(0, n):
        rotated_board[n - 1 - board[row]] = row
    if debug or '90' in debug_args:
        print('90', board, rotated_board)

    return summarize(rotated_board)


def rotate_180(board, n):
    # This function returns a 180 degree anti-clockwise rotation of the given board position.
    rotated_board = [0 for i in range(0, n)]
    for row in range(0, n):
        rotated_board[n - 1 - row] = n - 1 - board[row]
    if debug or '180' in debug_args:
        print('180', board, rotated_board)

    return summarize(rotated_board)


def rotate_270(board, n):
    # This function returns a 270 degree anti-clockwise rotation of the given board position.
    rotated_board = [0 for i in range(0, n)]
    for row in range(0, n):
        rotated_board[board[row]] = n - 1 - row
    if debug or '270' in debug_args:
        print('270', board, rotated_board)

    return summarize(rotated_board)


def reflect_leading(board, n):
    # This function returns a reflection in the leading diagonal of the given board position.
    reflected_board = [0 for i in range(0, n)]
    for row in range(0, n):
        reflected_board[board[row]] = row
    if debug or 'LDIAG' in debug_args:
        print('LDIAG', board, reflected_board)

    return summarize(reflected_board)


def reflect_trailing(board, n):
    # This function returns a reflection in the trailing diagonal of the given board position.
    reflected_board = [0 for i in range(0, n)]
    for row in range(0, n):
        reflected_board[n - 1 - board[row]] = n - 1 - row
    if debug or 'TDIAG' in debug_args:
        print('TDIAG', board, reflected_board)

    return summarize(reflected_board)


def reflect_horizontally(board, n):
    # This function returns a horizontal reflection of the given board position.
    reflected_board = [0 for i in range(0, n)]
    for row in range(0, n):
        reflected_board[n - 1 - row] = board[row]
    if debug or 'HORI' in debug_args:
        print('HORI', board, reflected_board)

    return summarize(reflected_board)


def reflect_vertical(board, n):
    # This function returns a vartical reflection of the given board position.
    reflected_board = [0 for i in range(0, n)]
    for row in range(0, n):
        reflected_board[row] = n - 1 - board[row]
    if debug or 'VERT' in debug_args:
        print('VERT', board, reflected_board)

    return summarize(reflected_board)


def check_unique(board, n, sol_count):
    #
    # This function computes 7 symmetries of the board position.  These are:
    #
    #  1. 90  degree rotation.
    #  2. 180 degree rotation.
    #  3. 270 degree rotation.
    #  4. 180 degree reflection about the top-left/bottom-right diagonal.
    #  5. 180 degree reflection about the bottom-left/top-right diagonal.
    #  6. 180 degree reflection about the horizontal mid-line.
    #  7. 180 degree reflection about the vertical mid-line.
    #
    unique_solution = True

    if sol_count > 0:
        # Compare all 7 symmetries with all previous solutions.
        rotated_90_board = rotate_90(board, n)
        rotated_180_board = rotate_180(board, n)
        rotated_270_board = rotate_270(board, n)

        reflected_leading_board = reflect_leading(board, n)
        reflected_trailing_board = reflect_trailing(board, n)
        reflected_horizontal_board = reflect_horizontally(board, n)
        reflected_vertical_board = reflect_vertical(board, n)

        for solution in solutions:
            if rotated_90_board == solution or \
               rotated_180_board == solution or \
               rotated_270_board == solution or \
               reflected_leading_board == solution or \
               reflected_trailing_board == solution or \
               reflected_horizontal_board == solution or \
               reflected_vertical_board == solution:
                   unique_solution = False

            if not unique_solution:
                break

    return unique_solution


def solve(board, row, n, unique, count_only):
    global sol_count

    if row == n:
        if unique:
            if check_unique(board, n, sol_count):
                sol_count += 1
                solutions.append(summarize(board))
                print_board(board, sol_count, n, count_only)
                if debug:
                    print('SOLS', solutions)
                    print()
        else:
            sol_count += 1
            print_board(board, sol_count, n, count_only)
        return

    for col in range(0, n):
        if col in cols_used or (row + col) in up_diags_used or (row - col) in down_diags_used:
            continue

        cols_used.add(col)
        up_diags_used.add(row + col)
        down_diags_used.add(row - col)
        board[row] = col

        # Solve the next row by calling ourself recursively.
        solve(board, row + 1, n, unique, count_only)

        # Now backtrack to find more solutions.
        cols_used.remove(col)
        up_diags_used.remove(row + col)
        down_diags_used.remove(row - col)
        board[row] = 0


def main():
    global debug
    global debug_args

    # Check for any command line args.
    parser = argparse.ArgumentParser(description='This program computes the solutions to the n-queens problem.  That is, how to place n-queens on a chessboard, so they cannot take each other.')
    parser.add_argument('-n', '--size', help='size of board', type=int, default=8)
    parser.add_argument('-a', '--all', help='compute/print non-unique solutions', action='store_true')
    parser.add_argument('-c', '--count', help='output only a count of the solutions', action='store_true')
    parser.add_argument('-d', '--debug', help='print some debugging output', action='store_true')
    parser.add_argument('-p', '--debug_args', help='only output debug at these points', default='[]', nargs='*')
    args = parser.parse_args()

    n = args.size
    unique = not args.all
    count_only = args.count
    debug = args.debug
    debug_args = args.debug_args

    version = 'V1.0'
    print('N-Queens Solver {}'.format(version))

    # Show the board size that will be used.
    if unique:
        print(f'Finding unique solutions using a {n}x{n} board...\n')
    else:
        print(f'Finding all (non-unique) solutions using a {n}x{n} board...\n')

    # Define an empty board of the given size.
    board = [0 for i in range(0, n)]

    # Take note of the start time and begin.
    start_time = time.time()
    solve(board, 0, n, unique, count_only)

    # Print the run-time.
    seconds = time.time() - start_time
    print('Duration:', time.strftime("%H:%M:%S", time.gmtime(seconds)), '\n')

if __name__ == '__main__':
    main()
