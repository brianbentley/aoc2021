"""Day 14 Part 1 of Advent of Code 2021"""
import sys
from collections import Counter


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        insertion_map = {}
        polymer = input_data.readline().strip()
        _ = input_data.readline()
        current = input_data.readline().strip()
        while current:
            pair, insertion = current.split(" -> ")
            insertion_map[pair] = insertion
            current = input_data.readline().strip()
    return polymer, insertion_map


def process_step(polymer, insertion_map):
    i = 0
    j = 2
    new_polymer = polymer[i]
    while j <= len(polymer):
        new_polymer += insertion_map[polymer[i:j]]
        new_polymer += polymer[i + 1]
        i += 1
        j += 1
    return new_polymer


def main(input_file, steps):
    polymer, insertion_map = process_input(input_file)
    print(f"Template: {polymer}")
    for step in range(1, steps + 1):
        polymer = process_step(polymer, insertion_map)
        # print(f"After step {step}: {polymer}")
    counter = Counter(polymer)
    result = max(counter.values()) - min(counter.values())
    print(result)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
