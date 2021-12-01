"""Day 1 Part 2 of Advent of Code 2021"""
import sys


def main(input_file):
    """count the number of times the sum of measurements in this sliding window increases from the previous sum."""
    with open(input_file) as input_data:
        input = input_data.readlines()

    counter = 0
    current = int(input[1])
    previous_one = int(input[0])
    previous_two = None
    current_sum = float("inf")

    for i in input[2:]:
        previous_two = previous_one
        previous_one = current
        previous_sum = current_sum
        current = int(i)
        current_sum = current + previous_one + previous_two
        if current_sum > previous_sum:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main(sys.argv[1])
