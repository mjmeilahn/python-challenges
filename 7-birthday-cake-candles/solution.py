#!/bin/python3

import math
import os
import random
import re
import sys

# BEGIN challenge
def birthdayCakeCandles(ar):
    ar.sort()
    filtered = filter(lambda a : a > 0, ar)
    filterList = list(filtered)
    listLen = len(filterList) - 1
    highest = filterList[listLen]
    amount = list(filterList)
    filteredAmt = filter(lambda a : a == highest, amount)
    finalList = list(filteredAmt)

    return len(finalList)
    # END challenge



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
