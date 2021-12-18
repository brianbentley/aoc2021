"""Day 13 Part 1 of Advent of Code 2021"""
import sys
from pprint import PrettyPrinter


def process_input(input_file):
    dots = []
    folds = []
    with open(input_file, encoding="utf8") as input_data:
        current = True
        while current:
            current = input_data.readline()
            if current == "\n":
                break
            dots.append(tuple([int(x) for x in current.split(",")]))
        current = input_data.readline()
        while current:
            location = current.split()[-1].split("=")
            fold = (location[0], int(location[1]))
            folds.append(fold)
            current = input_data.readline()
    return dots, folds


def create_matrix(dots):
    cols = max([x[0] for x in dots]) + 1
    rows = max([x[1] for x in dots]) + 1
    matrix = [[False] * cols for i in range(rows)]
    for x, y in dots:
        matrix[y][x] = True
    return matrix


def create_fold(matrix, axis, position):
    if axis == "x":
        new_matrix = [row[:position] for row in matrix]
        for i, j in zip(range(position), range(len(matrix[0]) - 1, position, -1)):
            for y in range(len(matrix)):
                new_matrix[y][i] = new_matrix[y][i] or matrix[y][j]
    else:
        new_matrix = matrix[:position]
        for i, j in zip(range(position), range(len(matrix) - 1, position, -1)):
            for x in range(len(matrix[0])):
                new_matrix[i][x] = matrix[i][x] or matrix[j][x]
    return new_matrix


def count_dots(matrix):
    counter = 0
    for row in matrix:
        for value in row:
            if value:
                counter += 1
    return counter


def main(input_file):
    dots, folds = process_input(input_file)
    matrix = create_matrix(dots)
    for fold in folds[:1]:
        axis, position = fold
        matrix = create_fold(matrix, axis, position)
        dot_count = count_dots(matrix)
        print(dot_count)


if __name__ == "__main__":
    main(sys.argv[1])
