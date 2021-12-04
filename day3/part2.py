"""Day 3 Part 2 of Advent of Code 2021"""
import sys
from collections import Counter


def read_input_file(input_file):
    with open(input_file, encoding="utf8") as input_data:
        measurements = [s.strip() for s in input_data.readlines()]
    return measurements


def calculate_oxygen_rating(measurements):
    oxygen_rating = [*measurements]
    index = 0
    while len(oxygen_rating) > 1:
        counter = Counter([x[index] for x in oxygen_rating])
        if counter["0"] > counter["1"]:
            filter_function = lambda x: x[index] == "0"
        else:
            filter_function = lambda x: x[index] == "1"
        oxygen_rating = list(filter(filter_function, oxygen_rating))
        index += 1
    return oxygen_rating[0]


def calculate_co2_rating(measurements):
    co2_rating = [*measurements]
    index = 0
    while len(co2_rating) > 1:
        counter = Counter([x[index] for x in co2_rating])
        if counter["0"] > counter["1"]:
            filter_function = lambda x: x[index] == "1"
        else:
            filter_function = lambda x: x[index] == "0"
        co2_rating = list(filter(filter_function, co2_rating))
        index += 1
    return co2_rating[0]


def calculate_life_support_rating(oxygen_rating, co2_rating):
    return int(oxygen_rating, 2) * int(co2_rating, 2)


def main(input_file):
    """Use the binary numbers in your diagnostic report to calculate the oxygen generator rating
    and CO2 scrubber rating, then multiply them together.
    What is the life support rating of the submarine?"""
    measurements = read_input_file(input_file)

    oxygen_rating = calculate_oxygen_rating(measurements)
    co2_rating = calculate_co2_rating(measurements)
    life_support_rating = calculate_life_support_rating(oxygen_rating, co2_rating)

    print(f"oxygen rating: {oxygen_rating}")
    print(f"co2 rating: {co2_rating}")
    print(f"life support rating: {life_support_rating}")


if __name__ == "__main__":
    main(sys.argv[1])
