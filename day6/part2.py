"""Day 6 Part 2 of Advent of Code 2021"""
import sys


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        lantern_fish = [int(i) for i in input_data.readline().split(',')]
    return lantern_fish


def build_fish_hash(lantern_fish):
    fish_hash = {}
    for fish in lantern_fish:
        fish_hash[fish] = fish_hash.get(fish, 0) + 1
    return fish_hash


def simulate_growth(lantern_fish):
    lantern_fish = {key - 1: value for key, value in lantern_fish.items()}
    lantern_fish[8] = lantern_fish.get(-1, 0)
    if 6 in lantern_fish:
        lantern_fish[6] += lantern_fish.get(-1, 0)
    else:
        lantern_fish[6] = lantern_fish.get(-1, 0)
    if -1 in lantern_fish:
        del lantern_fish[-1]
    return lantern_fish




def main(input_file, days):
    """Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?"""
    lantern_fish = process_input(input_file)
    fish_hash = build_fish_hash(lantern_fish)
    print(f"initial state: {fish_hash}")
    for day in range(1, days + 1):
        fish_hash = simulate_growth(fish_hash)
        print(f"after {day} days: {fish_hash}")
    print(f"total: {sum(fish_hash.values())}")



if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
