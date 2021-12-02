"""Day 2 Part 2 of Advent of Code 2021"""
import sys


def main(input_file):
    """Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?"""
    aim = 0
    horizontal_position = 0
    depth = 0
    with open(input_file) as input_data:
        newline = input_data.readline()
        while newline:
            direction, unit = newline.split(" ")
            unit = int(unit)
            if direction == "down":
                aim += unit
            elif direction == "up":
                aim -= unit
            elif direction == "forward":
                horizontal_position += unit
                depth += aim * unit
            newline = input_data.readline()

    product = horizontal_position * depth
    print(f"aim: {aim}")
    print(f"horizontal: {horizontal_position}")
    print(f"depth: {depth}")
    print(f"product: {product}")


if __name__ == "__main__":
    main(sys.argv[1])
