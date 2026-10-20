# Problem 13: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s):
    char_counts = Counter(s)                       # how often each character appears
    count_freq = Counter(char_counts.values())     # how many characters share each count

    if len(count_freq) == 1:
        return "YES"

    if len(count_freq) > 2:
        return "NO"

    (low, low_freq), (high, high_freq) = sorted(count_freq.items())

    # one character appears once: remove it completely
    if low == 1 and low_freq == 1:
        return "YES"

    # one character appears one extra time: remove one copy of it
    if high == low + 1 and high_freq == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(str(result) + '\n')

    fptr.close()
