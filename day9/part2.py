"""Day 9 Part 2 of Advent of Code 2021"""
import sys
from collections import deque


def process_input(input_file):
    height_map = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            height_map.append([int(x) for x in list(current.strip())])
            current = input_data.readline()
    return height_map


def get_neighbors(height_map, locations, row, col):
    neighbors = []
    for location in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if location in locations:
            neighbors.append(location)
    return neighbors


def find_basin(height_map, locations, row, col):
    basin = []
    queue = deque()
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        if (r, c) in locations:
            locations.remove((r, c))
            if height_map[r][c] != 9:
                basin.append((r, c))
                for neighbor in get_neighbors(height_map, locations, r, c):
                    queue.append(neighbor)
    return basin


def main(input_file):
    height_map = process_input(input_file)
    locations = [
        (r, c) for r in range(len(height_map)) for c in range(len(height_map[0]))
    ]
    basins = []
    while locations:
        r, c = locations[0]
        basin = find_basin(height_map, locations, r, c)
        if basin:
            basins.append(basin)
    top_basin_sizes = sorted([len(b) for b in basins], reverse=True)[:3]
    print(top_basin_sizes)
    product = 1
    for size in top_basin_sizes:
        product *= size
    print(product)


if __name__ == "__main__":
    main(sys.argv[1])
