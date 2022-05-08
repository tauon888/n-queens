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
