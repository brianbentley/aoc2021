"""Day 5 Part 2 of Advent of Code 2021"""
import sys
from pprint import PrettyPrinter


def process_input(input_file):
    lines = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            line = [[int(x) for x in t.split(",")] for t in current.split(" -> ")]
            lines.append(line)
            current = input_data.readline()
    return lines


def build_matrix(lines):
    max_x = max([t[0] for l in lines for t in l])
    max_y = max([t[1] for l in lines for t in l])
    matrix = []
    for _ in range(max_y + 1):
        matrix.append([0] * (max_x + 1))
    for start, end in lines:
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                matrix[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                matrix[y1][i] += 1
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            i = x1
            j = y1
            while i <= x2:
                matrix[j][i] += 1
                if y1 > y2:
                    j -= 1
                else:
                    j += 1
                i += 1

    return matrix


def count_dangerous_areas(matrix):
    counter = 0
    for row in matrix:
        for x in row:
            if x > 1:
                counter += 1
    return counter


def main(input_file):
    """To avoid the most dangerous areas, you need to determine
    the number of points where at least two lines overlap.
    Including diagnoals now!"""
    lines = process_input(input_file)
    matrix = build_matrix(lines)
    # printer = PrettyPrinter()
    # printer.pprint(lines)
    # printer.pprint(matrix)
    dangerous_areas = count_dangerous_areas(matrix)
    print(f"dangerous_areas: {dangerous_areas}")


if __name__ == "__main__":
    main(sys.argv[1])
