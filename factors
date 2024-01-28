#!/usr/bin/env python3

import sys


def factorize_number(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.rstrip())
            factors = factorize_number(number)
            if factors:
                print("{}={}*{}".format(number, factors[0], factors[1]))


if __name__ == "__main__":
    main()
