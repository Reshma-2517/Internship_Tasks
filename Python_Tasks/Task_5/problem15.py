# Problem 15: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    result = []

    for _ in range(N):
        parts = input().split()
        command = parts[0]
        args = list(map(int, parts[1:]))

        if command == "insert":
            result.insert(args[0], args[1])
        elif command == "print":
            print(result)
        elif command == "remove":
            result.remove(args[0])
        elif command == "append":
            result.append(args[0])
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result.reverse()
