# Problem 20: No Idea!
# HackerRank Link: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0
for value in arr:
    if value in set_a:
        happiness += 1
    elif value in set_b:
        happiness -= 1

print(happiness)
