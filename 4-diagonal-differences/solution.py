#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# BEGIN challenge
def diagonalDifference(arr):
    size = len(arr) - 1
    row = len(arr[0]) - 1
    left = []
    right = []
    counter = 0

    # CALCULATE LEFT
    for i in arr:
        left.append(i[counter])
        counter += 1

    Ltotal = reduce(lambda a, b : a + b, left)

    # CALCULATE RIGHT & RESET COUNTER
    counter = 0
    arr.reverse()
    for i in arr:
        right.append(i[counter])
        counter += 1

    Rtotal = reduce(lambda a, b : a + b, right)

    return abs(Ltotal - Rtotal)
    # END challenge


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
