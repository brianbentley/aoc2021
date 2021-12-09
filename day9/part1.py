"""Day 9 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    height_map = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            height_map.append([int(x) for x in list(current.strip())])
            current = input_data.readline()
    return height_map


def check_lowpoint(height_map, row, col):
    rows = [row]
    cols = [col]
    if row > 0:
        rows.append(row - 1)
    if row < len(height_map) - 1:
        rows.append(row + 1)
    if col > 0:
        cols.append(col - 1)
    if col < len(height_map[row]) - 1:
        cols.append(col + 1)
    locations = [(r, c) for r in rows for c in cols]
    for r, c in locations:
        if height_map[r][c] < height_map[row][col]:
            return False
    return True


def calculate_risk(low_poiints):
    accumulator = 0
    for height in low_poiints:
        accumulator += height + 1
    return accumulator


def main(input_file):
    height_map = process_input(input_file)
    low_points = []
    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if check_lowpoint(height_map, row, col):
                low_points.append(height_map[row][col])

    risk_score = calculate_risk(low_points)
    print(risk_score)


if __name__ == "__main__":
    main(sys.argv[1])
