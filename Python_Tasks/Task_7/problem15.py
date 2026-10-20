# Problem 15: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def gameOfThrones(s):
    counts = Counter(s)
    odd = 0
    for value in counts.values():
        if value % 2 == 1:
            odd += 1
    # a palindrome can have at most one character with an odd count
    if odd <= 1:
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(str(result) + '\n')

    fptr.close()
