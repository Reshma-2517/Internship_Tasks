# Problem 11: String Formatting
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)) - 2   # length of the binary form of number

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
