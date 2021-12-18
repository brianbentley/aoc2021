"""Day 14 Part 2 of Advent of Code 2021"""
import sys
from collections import Counter


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        rules = {}
        polymer = input_data.readline().strip()
        _ = input_data.readline()
        current = input_data.readline().strip()
        while current:
            pair, rule = current.split(" -> ")
            rules[pair] = rule
            current = input_data.readline().strip()
    return polymer, rules


def main(input_file, steps):
    polymer, rules = process_input(input_file)
    chars = Counter(polymer)
    pairs = Counter(["".join(s) for s in zip(polymer, polymer[1:])])
    for _ in range(steps):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c
    print(max(chars.values()) - min(chars.values()))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
