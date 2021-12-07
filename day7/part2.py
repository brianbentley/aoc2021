"""Day 7 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        position_list = [int(i) for i in input_data.readline().split(",")]
    return position_list


def calculate_distance(position_list, target_position):
    accumulator = 0
    for position in position_list:
        fuel = sum(range(abs(position - target_position) + 1))
        accumulator += fuel
    return accumulator


def main(input_file):
    position_list = process_input(input_file)

    min_fuel = float("inf")
    min_fuel_position = None

    low = min(position_list)
    high = max(position_list) + 1

    for i in range(low, high):
        current_fuel = calculate_distance(position_list, i)
        if current_fuel < min_fuel:
            min_fuel = current_fuel
            min_fuel_position = i

    print(f"minimum fuel: {min_fuel}")
    print(f"minimum fuel position: {min_fuel_position}")


if __name__ == "__main__":
    main(sys.argv[1])
