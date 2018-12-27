#!/bin/python3

import os
import sys
from functools import reduce

# BEGIN challenge
def simpleArraySum(ar):
    return reduce(lambda a, b : a + b, ar)
    # END challenge

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
