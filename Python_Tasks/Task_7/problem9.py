# Problem 9: Beautiful Binary String
# HackerRank Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    # each "010" needs one change; changing its last character also
    # breaks any overlapping "010", so count non-overlapping matches
    changes = 0
    i = 0
    while i <= len(b) - 3:
        if b[i:i + 3] == "010":
            changes += 1
            i += 3
        else:
            i += 1
    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
