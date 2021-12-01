"""Day 1 Part 1 of Advent of Code 2021"""
import sys


def main(input_file):
    """count the number of times a depth measurement increases from the previous measurement.
    (There is no measurement before the first measurement.)"""
    with open(input_file) as input_data:
        input = input_data.readlines()

    counter = 0
    current = int(input[0])
    for i in input[1:]:
        previous = current
        current = int(i)
        if current > previous:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main(sys.argv[1])
