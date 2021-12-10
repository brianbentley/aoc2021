"""Day 10 Part 1 of Advent of Code 2021"""
import sys


PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def process_input(input_file):
    lines = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            lines.append(current.strip())
            current = input_data.readline()
    return lines


def check_balance(line):
    stack = [None]
    for char in line:
        if char in PAIRS:
            if stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                return POINTS[char]
        elif char in PAIRS.values():
            stack.append(char)
    return 0


def main(input_file):
    lines = process_input(input_file)
    results = [check_balance(line) for line in lines]
    print(sum(results))


if __name__ == "__main__":
    main(sys.argv[1])
