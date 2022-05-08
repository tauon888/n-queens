# n-queens
Python script to solve the n-queens problem.

This is based on:

1. Thorsten Altenkirk's excellent book:

   Conceptual Programming in Python - http://www.cs.nott.ac.uk/~pszit/cp.html

2. Neetcode's excellent algorithm for testing column and diagonal occupancy
using sets - https://www.youtube.com/watch?v=Ph95IHmRp5M

## Statistics
| Board Size | Unique Solutions | Total Solutions | Run Time<sup>1</sup> | Run Time<sup>2</sup> |
| ---------: | ---------------: | --------------: | :-------------------: | :-----------------: |
|  1 | 1 |       1 | 00:00:00 | 00:00:00 |
|  2 | 0 |       0 | 00:00:00 | 00:00:00 |
|  3 | 0 |       0 | 00:00:00 | 00:00:00 |
|  4 | 2 |       2 | 00:00:00 | 00:00:00 |
|  5 |   |      10 | 00:00:00 | 00:00:00 |
|  6 |   |       4 | 00:00:00 | 00:00:00 |
|  7 |   |      40 | 00:00:00 | 00:00:00 |
|  8 |   |      92 | 00:00:00 | 00:00:00 |
|  9 |   |     352 | 00:00:02 | 00:00:00 |
| 10 |   |     724 | 00:00:04 | 00:00:00 |
| 11 |   |   2,680 | 00:00:20 | 00:00:00 |
| 12 |   |  14,200 | 00:01:59 | 00:00:00 |
| 13 |   |  73,712 | 00:10:18 | 00:00:00 |
| 14 |   | 365,596 | 01:01:03 | 00:00:00 |

- Note <sup>1</sup> - Timings based on my original diagonal checking
- Note <sup>2</sup> - Timings based on Neetcode's diagonal checking

Original Diagonal Checking Logic...
5 x 5 board example
<!--
|           | col 0 | col 1 | col 2 |  col 3| col 4 |
| :-------: | :---: | :---: | :---: | :---: | :---: |
| **row 0** | (0,0) | (0,1) | (0,2) | (0,3) | (0,4) |
| **row 1** | (1,0) | (1,1) | (1,2) | (1,3) | (1,4) |
| **row 2** | (2,0) | (2,1) | (2,2) | (2,3) | (2,4) |
| **row 3** | (3,0) | (3,1) | (3,2) | (3,3) | (3,4) |
| **row 4** | (4,0) | (4,1) | (4,2) | (4,3) | (4,4) |
-->
### Leading/Down Diagonals
|           | col 0 | col 1 | col 2 |  col 3| col 4 |
| :-------: | :---: | :---: | :---: | :---: | :---: |
| **row 0** | <span style="color:red">(0,0)</span> | <span style="color:yellow">(0,1)</span> | <span style="color:green">(0,2)</span> | <span style="color:orange">(0,3)</span> | (0,4) |
| **row 1** | <span style="color:cyan">(1,0)</span> | <span style="color:red">(1,1)</span> | <span style="color:yellow">(1,2)</span> | <span style="color:green">(1,3)</span> | <span style="color:orange">(1,4)</span> |
| **row 2** | <span style="color:salmon">(2,0)</span> | <span style="color:cyan">(2,1)</span> | <span style="color:red">(2,2)</span> | <span style="color:yellow">(2,3)</span> | <span style="color:green">(2,4)</span> |
| **row 3** | <span style="color:magenta">(3,0)</span> | <span style="color:salmon">(3,1)</span> | <span style="color:cyan">(3,2)</span> | <span style="color:red">(3,3)</span> | <span style="color:yellow">(3,4)</span> |
| **row 4** | (4,0) | <span style="color:magenta">(4,1)</span> | <span style="color:salmon">(4,2)</span> | <span style="color:cyan">(4,3)</span> | <span style="color:red">(4,4)</span> |

```

    # Leading-Down (\) diagonal test.
    if row == col:
        # The main down diagonal.
        for r in range(0, grid_size):
            if grid[r][r] == 'Q':
                return False
    elif row > col:
        # Down diagonals under the main diagonal.
        # Top of diagonal is (row - col, 0), down to (grid_size - 1, grid_size - row + col).
        # Note the use of zip to glue these 2 ranges together.
        start_row = row - col
        for r, c in zip(range(start_row, grid_size), range(0, grid_size + 1 - start_row)):
            if grid[r][c] == 'Q':
                return False
    else:
        # Down diagonals above the main diagonal.
        # Top of diagonal is (0, col - row), down to (col - row, grid_size - 1).
        # Note the use of zip to glue these 2 ranges together.
        start_col = col - row
        for r, c in zip(range(0, grid_size - start_col), range(start_col, grid_size)):
            if grid[r][c] == 'Q':
                return False
```
### Trailing/Up Diagonals
|           | col 0 | col 1 | col 2 |  col 3| col 4 |
| :-------: | :---: | :---: | :---: | :---: | :---: |
| **row 0** | (0,0)</span> | <span style="color:orange;">(0,1)</span> | <span style="color:green">(0,2)</span> | <span style="color:yellow">(0,3)</span> | <span style="color:red">(0,4)</span> |
| **row 1** | <span style="color:orange">(1,0)</span> | <span style="color:green">(1,1)</span> | <span style="color:yellow">(1,2)</span> | <span style="color:red">(1,3)</span> | <span style="color:cyan">(1,4)</span> |
| **row 2** | <span style="color:green">(2,0)</span> | <span style="color:yellow">(2,1)</span> | <span style="color:red">(2,2)</span> | <span style="color:cyan">(2,3)</span> | <span style="color:salmon">(2,4)</span> |
| **row 3** | <span style="color:yellow">(3,0)</span> | <span style="color:red">(3,1)</span> | <span style="color:cyan">(3,2)</span> | <span style="color:salmon">(3,3)</span> | <span style="color:magenta">(3,4)</span> |
| **row 4** | <span style="color:red">(4,0)</span> | <span style="color:cyan">(4,1)</span> | <span style="color:salmon">(4,2)</span> | <span style="color:magenta">(4,3)</span> | (4,4) |

```
# Trailing-Up (/) diagonal test.
sum = row + col
start_row = 0
stop_row = 0
if sum <= grid_size - 1:
    # Above or on the trailing diagonal.
    # Start at (0, row + col) down to (row + col, 0)
    start_row = 0
    stop_row = sum + 1
else:
    # Under the trailing diagonal.
    # Start at (row + col - grid_size + 1, grid_size - 1) down to (grid_size - 1, )
    start_row = sum - (grid_size - 1)
    stop_row = grid_size - 1

for r in range(start_row, stop_row + 1):
    if grid[r][sum-r] == 'Q':
            return False
```

## Sample run
```
python n-queens.py
Board size, n? 5
Using an 5 x 5 board
Solution: 1
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
Solution: 2
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
Solution: 3
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
Solution: 4
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
Solution: 5
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
Solution: 6
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
Solution: 7
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
Solution: 8
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
Solution: 9
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
Solution: 10
+---+---+---+---+---+
|   |   |   |   | Q |
+---+---+---+---+---+
|   |   | Q |   |   |
+---+---+---+---+---+
| Q |   |   |   |   |
+---+---+---+---+---+
|   |   |   | Q |   |
+---+---+---+---+---+
|   | Q |   |   |   |
+---+---+---+---+---+
Duration: 00:00:00
```
