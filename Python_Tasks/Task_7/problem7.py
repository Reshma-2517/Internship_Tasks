# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    rows = []

    for i in range(size):
        # letters from the largest down to alphabet[size-1-i], then back up
        left = alphabet[size - 1:size - 1 - i:-1] if i > 0 else ""
        letters = list(left) + [alphabet[size - 1 - i]] + list(left[::-1])
        rows.append("-".join(letters).center(width, "-"))

    # top half, middle row, then the top half mirrored
    for row in rows:
        print(row)
    for row in reversed(rows[:-1]):
        print(row)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
