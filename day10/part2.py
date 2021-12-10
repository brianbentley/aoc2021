"""Day 10 Part 1 of Advent of Code 2021"""
import sys


PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
POINTS = {"(": 1, "[": 2, "{": 3, "<": 4}


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
    score = 0
    for char in line:
        if char in PAIRS:
            if stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                return 0
        elif char in PAIRS.values():
            stack.append(char)
    if len(stack) > 1:
        for i in range(len(stack) - 1, 0, -1):
            score *= 5
            score += POINTS[stack[i]]
    return score


def main(input_file):
    lines = process_input(input_file)
    results = [check_balance(line) for line in lines]
    results = list(filter(lambda x: x != 0, results))
    results.sort()
    print(results)
    print(results[len(results) // 2])


if __name__ == "__main__":
    main(sys.argv[1])
