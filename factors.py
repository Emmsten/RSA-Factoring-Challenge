#!/usr/bin/python3

import sys

def factorize(number):
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize(number)
            if factorizations:
                for factors in factorizations:
                    print(f"{number}={factors[0]}*{factors[1]}")
except FileNotFoundError:
    print(f"File '{sys.argv[1]}' not found.")
    sys.exit(1)
except ValueError:
    print(f"Invalid input in '{sys.argv[1]}' - Please make sure all lines are valid natural numbers greater than 1.")
    sys.exit(1)
