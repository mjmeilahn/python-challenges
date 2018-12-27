#!/bin/python3

import math
import os
import random
import re
import sys

# BEGIN challenge
def countApplesAndOranges(s, t, a, b, apples, oranges):
    if s == 0:
        begin = 1
    else:
        begin = s

    if t == 0:
        end = 1
    else:
        end = t

    appleList = []
    orangeList = []

    for apple in apples:
        value = apple + a
        appleList.append(value)

    for orange in oranges:
        value = orange + b
        orangeList.append(value)

    finalA = filter(lambda app : app >= begin and app <= end, appleList)
    finalO = filter(lambda org : org >= begin and org <= end, orangeList)

    aList = list(finalA)
    oList = list(finalO)

    print(len(aList))
    print(len(oList))
    # END challenge


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
