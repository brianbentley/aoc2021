"""Day 11 Part 2 of Advent of Code 2021"""
import sys
from pprint import PrettyPrinter
from collections import deque


def process_input(input_file):
    energy_levels = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            energy_levels.append([int(x) for x in current.strip()])
            current = input_data.readline()
    return energy_levels


def get_neighbors(grid, row, col):
    neighbors = []
    rows = []
    cols = []
    for r in [row - 1, row, row + 1]:
        if r >= 0 and r < len(grid):
            rows.append(r)
    for c in [col - 1, col, col + 1]:
        if c >= 0 and c < len(grid[0]):
            cols.append(c)
    for r in rows:
        for c in cols:
            if r != row or c != col:
                neighbors.append((r, c))
    return neighbors


def process_step(energy_levels):
    flash_count = 0
    flash_queue = deque()
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[row])):
            current_level = energy_levels[row][col]
            current_level += 1
            if current_level == 10:
                flash_queue.append((row, col))
                current_level = 0
            energy_levels[row][col] = current_level
    while flash_queue:
        row, col = flash_queue.popleft()
        flash_count += 1
        for nr, nc in get_neighbors(energy_levels, row, col):
            current_neighbor = energy_levels[nr][nc]
            if current_neighbor != 0:
                current_neighbor += 1
                if current_neighbor == 10:
                    flash_queue.append((nr, nc))
                    current_neighbor = 0
                energy_levels[nr][nc] = current_neighbor
    return flash_count


def main(input_file):
    energy_levels = process_input(input_file)
    level_count = len(energy_levels) * len(energy_levels[0])
    steps = 10000
    flash_count = 0
    for step in range(steps):
        current_flash_count = process_step(energy_levels)
        flash_count += current_flash_count
        if current_flash_count == level_count:
            print(step + 1)
            break
    printer = PrettyPrinter()
    printer.pprint(energy_levels)
    print(flash_count)


if __name__ == "__main__":
    main(sys.argv[1])
