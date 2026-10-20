# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split()))
n = int(input())
is_strict_superset = True

for _ in range(n):
    other = set(map(int, input().split()))
    # strict superset: contains every element of other AND has something extra
    if not (set_a > other):
        is_strict_superset = False

print(is_strict_superset)
