# Problem 19: Merge the Tools!
# HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for start in range(0, len(string), k):
        part = string[start:start + k]
        seen = set()
        result = ""
        for ch in part:
            if ch not in seen:
                seen.add(ch)
                result += ch
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
