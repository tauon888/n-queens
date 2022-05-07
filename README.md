# n-queens
Python script to solve the n-queens problem.

This is based on:

1. Thorsten Altenkirk's excellent book:

   Conceptual Programming in Python - http://www.cs.nott.ac.uk/~pszit/cp.html

2. Neetcode's excellent algorithm for testing column and diagonal occupancy
using sets - https://www.youtube.com/watch?v=Ph95IHmRp5M


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
