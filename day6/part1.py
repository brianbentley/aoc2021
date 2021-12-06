"""Day 6 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        lantern_fish = [int(i) for i in input_data.readline().split(',')]
    return lantern_fish


def simulate_growth(lantern_fish):
    for i in range(len(lantern_fish)):
        if lantern_fish[i] == 0:
            lantern_fish[i] = 6
            lantern_fish.append(8)
        else:
            lantern_fish[i] -= 1
    return lantern_fish


def main(input_file, days):
    """Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?"""
    lantern_fish = process_input(input_file)
    print(f"initial state: {lantern_fish}")
    for day in range(1, days + 1):
        lantern_fish = simulate_growth(lantern_fish)
        print(f"after {day} days: {len(lantern_fish)}")
    print(f"total: {len(lantern_fish)}")



if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
