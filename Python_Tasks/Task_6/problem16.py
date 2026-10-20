# Problem 16: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    na = int(input())
    set_a = set(map(int, input().split()))
    nb = int(input())
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
