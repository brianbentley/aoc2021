"""Day 7 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        position_list = [int(i) for i in input_data.readline().split(",")]
    return position_list


def calculate_distance(position_list, target_position):
    accumulator = 0
    for position in position_list:
        accumulator += abs(position - target_position)
    return accumulator


def main(input_file):
    position_list = process_input(input_file)
    position_list.sort()
    min_fuel = (None, float("inf"))
    for position in position_list:
        current_fuel = calculate_distance(position_list, position)
        if current_fuel < min_fuel[1]:
            min_fuel = (position, current_fuel)
    print(f"minimum fuel: {min_fuel}")


if __name__ == "__main__":
    main(sys.argv[1])
