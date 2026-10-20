# Problem 14: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def anagram(s):
    if len(s) % 2 == 1:
        return -1
    half = len(s) // 2
    first = Counter(s[:half])
    second = Counter(s[half:])
    # characters in the first half that the second half is missing
    return sum((first - second).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
