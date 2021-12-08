"""Day 8 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    display_signals = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            display_signals.append([s.split() for s in current.split(" | ")])
            current = input_data.readline()
    return display_signals


def main(input_file):
    display_signals = process_input(input_file)
    display_output = [l[1] for l in display_signals]
    unique_segment_count = 0
    for entry in display_output:
        for segment in entry:
            if len(segment) in [2, 4, 3, 7]:
                unique_segment_count += 1
    print(f"unique_segment_count: {unique_segment_count}")


if __name__ == "__main__":
    main(sys.argv[1])
