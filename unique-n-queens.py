#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#      Name:  unique-n-queens.py
#   Purpose:  Uses symmetry checking to find unqiue n-queens solutions.
#
#    Author:  Mike Smith 
#             (Ported to Python from my 27-Nov-1988 Pascal implementation!)
#
#   Created:  26/07/2022
# Copyright:  (c) Mike 2022
# Reference:  https://en.wikipedia.org/wiki/Eight_queens_puzzle
#-------------------------------------------------------------------------------
import time
"""
Created on Tue Jul 26 13:35:25 2022

@author: mike
"""

board_size = 0
sol_count = 0
row_pos = [0]*21
positions = [[0]*21 for i in range(20001)]
remove_symmetries = True

def summarize(new_pos):
    """ This function returns an integer summary of the position. """
    
    n = 0
    for i in range(1, board_size+1):
        n += new_pos[i] * (10**(board_size-i))
    
    return n


def rotate(row_pos):
    """ This performs a rotation on the position and summarises it. """

    new_pos = [0]*21
    for i in range(board_size, 0, -1):
        for j in range(1, board_size+1):
            if row_pos[j] == i:
                new_pos[board_size+1-i] = j

    #for i in range(1, board_size+1):
    #    row_pos[i] = new_pos[i]
        
    return summarize(new_pos), new_pos
                

def reflect_horizontal(row_pos):
    """ This performs a horizontal reflection and summarises it. """

    new_pos = [0]*21
    for i in range(1, board_size+1):
        new_pos[board_size+1-i] = row_pos[i]
       
    return summarize(new_pos)
    
    
def reflect_vertical(row_pos):
    """ This performs a vertical reflection and summarises it. """

    new_pos = [0]*21
    for i in range(1, board_size+1):
        new_pos[i] = board_size + 1 - row_pos[i]
       
    return summarize(new_pos)
    
    
def reflect_leading(row_pos):
    """ This performs a horizontal reflection and summarises it. """

    new_pos = [0]*21
    for i in range(1, board_size+1):
        new_pos[row_pos[i]] = i
       
    return summarize(new_pos)
    
    
def reflect_trailing(row_pos):
    """ This performs a horizontal reflection and summarises it. """

    new_pos = [0]*21
    for i in range(1, board_size+1):
        new_pos[board_size + 1 - row_pos[i]] = board_size + 1 - i
       
    return summarize(new_pos)
    
    
def printboard(row_pos):
    """ This function prints a solution. """
    
    print()
    print()
    print('{:3d}  '.format(sol_count), end='')
    for i in range(1, board_size+1):
        print('     {}'.format(chr(64+i)), end='')
    print()
    
    for i in range(1, board_size+1):
        print('       I', end='')
        for j in range(1, board_size+1):
            print('-----I', end='')
        print()
        print('    {:2d} I'.format(i), end='')

        for j in range(1, board_size+1):
            print('  ', end='')
            if row_pos[i] == j:
                print('Q', end='')
            else:
                print(' ', end='')
            print('  I', end='')
        print()
            
    print('       I', end='')
    for i in range(1, board_size+1):
        print('-----I', end='')
    print()
    print('     ', end='')
    for i in range(1, board_size+1):
        print('     {}'.format(chr(64+i)), end='')
    print()
        

def analyse_solution(row_pos):
    """
    This function looks at the solution in the array row_pos and computes
    7 symmetries of it.  These are:
        
    1. 90  degree rotation.
    2. 180 degree rotation.
    3. 270 degree rotation.
    4. 180 degree reflection about the top-left/bottom-right diagonal.
    5. 180 degree reflection about the bottom-left/top-right diagonal.
    6. 180 degree reflection about the horizontal mid-line.
    7. 180 degree reflection about the vertical mid-line.

    row_pos - array holding the current position of each queen on each row.

    """
    global sol_count
    global positions
    
    
    sol_count += 1
    new_solution = True

    # Compute all symmetries of the position.    
    positions[sol_count][1] = summarize(row_pos)
    
    positions[sol_count][2], new_pos = rotate(row_pos)
    #print("90 rotation: ", row_pos, new_pos)
    positions[sol_count][3], new_pos = rotate(new_pos)
    #print("90 rotation: ", new_pos)
    positions[sol_count][4], new_pos = rotate(new_pos)
    #print("90 rotation: ", new_pos)

    positions[sol_count][5] = reflect_leading(row_pos)
    positions[sol_count][6] = reflect_trailing(row_pos)
    positions[sol_count][7] = reflect_horizontal(row_pos)
    positions[sol_count][8] = reflect_vertical(row_pos)

    # Compare all 8 with all previous positions.
    if remove_symmetries:
        if sol_count > 1:
            i = 1
            while True:
                if positions[sol_count][1] == positions[i][1] or \
                   positions[sol_count][1] == positions[i][2] or \
                   positions[sol_count][1] == positions[i][3] or \
                   positions[sol_count][1] == positions[i][4] or \
                   positions[sol_count][1] == positions[i][5] or \
                   positions[sol_count][1] == positions[i][6] or \
                   positions[sol_count][1] == positions[i][7] or \
                   positions[sol_count][1] == positions[i][8]:
                       new_solution = False
                       
                i += 1
                if not new_solution or i == sol_count:
                    break
            
    if new_solution:
        printboard(row_pos)
    else:
        sol_count -= 1
    
    
def position_queen_on_row(row_pos, row_number):
    """ 
    Recursively find the solutions by evaluating all the combinations
    of putting a queen on each of the squares on each row.
    
    row_pos    - array holding the current position of each queen on each row.
    row_number - the current row that is being looked at.
    sol_count  - the counter of the solutions.
    board_size - the size of the chessboard.
    
    """
    #print('row_pos: {}, row_number: {}, sol_count: {}, board_size: {}'.format(row_pos, row_number, sol_count, board_size))
    valid_position = True

    for i in range(1, board_size+1):
        row_pos[row_number] = i
        valid_position = True
        if row_number > 1:
            for j in range(row_number-1, 0, -1):
                if (row_pos[row_number] == row_pos[j]) or \
                    (row_pos[row_number] == row_pos[j] - (row_number - j)) or \
                    (row_pos[row_number] == row_pos[j] + (row_number - j)):
                        valid_position = False
        
        if valid_position:
            if row_number != board_size:
                # print("Moving to next level {}...".format(row_number+1))
                position_queen_on_row(row_pos, row_number+1)
            else:
                analyse_solution(row_pos)
                

def main():
    global board_size
    global remove_symmetries
    
    #remove_symmetries = False
    
    start_time = time.time()      
    while True:
        try:
            board_size = int(input("Type in the size of the chessboard, (4-20) [8]? "))
        except ValueError:
            print("Please input a number")
            continue     
        
        if board_size >= 4 and board_size <= 20:
            position_queen_on_row(row_pos, 1)
            break
        else:
            print('Enter board size between 5-20')
    
    # Print the run-time.
    seconds = time.time() - start_time
    print('Duration:', time.strftime("%H:%M:%S", time.gmtime(seconds)), '\n')


if __name__ == '__main__':
    main()