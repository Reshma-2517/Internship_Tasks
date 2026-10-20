# Problem 20: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())
pattern = r"^[789]\d{9}$"

for _ in range(n):
    number = input().strip()
    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")
