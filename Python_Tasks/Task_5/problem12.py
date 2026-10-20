# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    words = s.split(" ")
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word[0].upper() + word[1:])
        else:
            capitalized.append(word)
    return " ".join(capitalized)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
