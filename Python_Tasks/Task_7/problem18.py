# Problem 18: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def stringConstruction(s):
    # each new distinct character costs 1; repeats can be copied for free
    return len(set(s))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
