# Problem 20: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))

    left = 0
    right = n - 1
    top = float("inf")
    possible = True

    while left <= right:
        # always pick the larger of the two ends
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1

        if current > top:
            possible = False
            break
        top = current

    print("Yes" if possible else "No")
