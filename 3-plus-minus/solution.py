#!/bin/python3

import math
import os
import random
import re
import sys

# BEGIN challenge
def plusMinus(arr):
    denom = len(arr)
    positives = []
    negatives = []
    zeroes = []

    for num in arr:
        if num == 0 : zeroes.append(1)
        elif num > 0 and num <= 100 : positives.append(1)
        elif num < 0 and num >= -100 : negatives.append(1)

    positiveAmt = round(len(positives), 6) / denom
    negativeAmt = round(len(negatives), 6) / denom
    zeroAmt = round(len(zeroes), 6) / denom

    print(positiveAmt) if positiveAmt > 0 else print(0)
    print(negativeAmt) if negativeAmt > 0 else print(0)
    print(zeroAmt) if zeroAmt > 0 else print(0)
    # END challenge

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
