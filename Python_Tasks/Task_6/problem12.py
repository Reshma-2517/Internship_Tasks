# Problem 12: Set .discard(), .remove() & .pop()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for _ in range(commands):
    parts = input().split()
    if parts[0] == "pop":
        s.pop()
    elif parts[0] == "remove":
        s.remove(int(parts[1]))
    elif parts[0] == "discard":
        s.discard(int(parts[1]))

print(sum(s))
