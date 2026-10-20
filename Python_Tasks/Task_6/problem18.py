# Problem 18: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

a_len = int(input())
set_a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    operation, _length = input().split()
    other = set(map(int, input().split()))

    if operation == "update":
        set_a.update(other)
    elif operation == "intersection_update":
        set_a.intersection_update(other)
    elif operation == "difference_update":
        set_a.difference_update(other)
    elif operation == "symmetric_difference_update":
        set_a.symmetric_difference_update(other)

print(sum(set_a))
