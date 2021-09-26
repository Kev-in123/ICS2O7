Answer
2.0/5
0
tostuti

    Expert
    271 answers
    58K people helped

Answer:

In order to get following pattern, we have to use numpy package.

Following code with work perfectly fine and will print the pattern.

Python code starts as below

*********************************************

# Python program to print 8 X 8 alternative 1 and 0's. 3rd and 4th row with all 0's

# checkerboard pattern using numpy

# We need Following pattern

# 0 1 0 1 0 1 0 1

# 1 0 1 0 1 0 1 0

# 0 1 0 1 0 1 0 1

# 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0

# 1 0 1 0 1 0 1 0

# 0 1 0 1 0 1 0 1

# 1 0 1 0 1 0 1 0

import numpy as np

# function to print Checkerboard pattern

def printcheckboard(n):

       print(" Customized Checkerboard pattern:")

       # create a n * n matrix  

       x = np.zeros((n, n), dtype = int)

       y = np.zeros((n, n), dtype = int)

       # fill with 1 the alternate rows and columns

       x[1::2, ::2] = 1

       x[::2, 1::2] = 1

      # fill with 0 the alternate rows and columns

       y[1::2, ::2] = 0

       y[::2, 1::2] = 0

       # print the pattern  for first 3 rows

       for i in range(0,3):

               for j in range(n):

                       print(x[i][j], end =" ")

               print()

       # print the pattern   for next two rows with all 0's

       for k in range(3,5):

               for l in range(n):

                       print(y[k][l], end =" ")

               print()

        # print the pattern  for last 3 rows with alternative 1 and 0.        

       for i in range(5,8):

               for j in range(n):

                       print(x[i][j], end =" ")

               print()

# Calling the function code

n = 8

printcheckboard(n)