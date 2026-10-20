# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()

    counts = Counter(s)
    # sort by count (highest first), then alphabetically for ties
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    for ch, count in ordered[:3]:
        print(ch, count)
