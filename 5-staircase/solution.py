#!/bin/python3

import math
import os
import random
import re
import sys

# BEGIN challenge
def staircase(n):
    if n > 0:
        str = ''
        spaces = []

    for i in range(1, n + 1):
        str = ' ' * (n - i)
        str += '#' * i if i != 1 else '#'
        print(str)
        # END challenge

if __name__ == '__main__':
    n = int(input())

    staircase(n)
