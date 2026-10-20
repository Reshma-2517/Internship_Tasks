# Problem 19: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    run_weight = 0

    for ch in s:
        weight = ord(ch) - ord('a') + 1
        if ch == previous:
            run_weight += weight
        else:
            run_weight = weight
        weights.add(run_weight)
        previous = ch

    result = []
    for q in queries:
        result.append("Yes" if q in weights else "No")
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
