#!/bin/python3

import math
import os
import random
import re
import sys

# BEGIN challenge
def compareTriplets(a, b):
    arr = []
    pointsA = 0
    pointsB = 0

    for i in range(3):
        if a[i] > b[i] : pointsA += 1
        if a[i] < b[i] : pointsB += 1

    arr.append(pointsA)
    arr.append(pointsB)

    return arr
    # END challenge


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
