#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# BEGIN challenge
def miniMaxSum(arr):
    arr.sort()
    min = filter(lambda a : a > 0, arr)
    max = filter(lambda a : a > 0, arr)

    min = list(min)
    max = list(max)

    min.pop(0)
    max.pop()

    minTotal = reduce(lambda a, b : a + b, min)
    maxTotal = reduce(lambda a, b : a + b, max)

    return print("{} {}".format(maxTotal, minTotal))
    # END challenge


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
