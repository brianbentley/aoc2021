"""Day 2 Part 1 of Advent of Code 2021"""
import sys


def main(input_file):
    """Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?"""
    direction_map = {}
    with open(input_file) as input_data:
        newline = input_data.readline()
        while newline:
            direction, unit = newline.split(" ")
            unit = int(unit)
            direction_map[direction] = direction_map.get(direction, 0) + unit
            newline = input_data.readline()

    horizontal_position = direction_map["forward"]
    depth = direction_map["down"] - direction_map["up"]
    product = horizontal_position * depth
    print(direction_map)
    print(f"horizontal: {horizontal_position}")
    print(f"depth: {depth}")
    print(f"product: {product}")


if __name__ == "__main__":
    main(sys.argv[1])
