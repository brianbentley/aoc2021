"""Day 12 Part 1 of Advent of Code2021"""
import sys
from collections import deque
from pprint import PrettyPrinter


def process_input(input_file):
    graph = {}
    with open(input_file, encoding="utf8") as input_data:
        for line in input_data:
            node, neighbor = line.strip().split("-")
            if node in graph:
                graph[node].append(neighbor)
            else:
                graph[node] = [neighbor]
            if neighbor in graph:
                graph[neighbor].append(node)
            else:
                graph[neighbor] = [node]
    return graph


def traverse(graph, node, explored, path, paths):
    if node.islower():
        explored[node] = True
    path.append(node)
    if node == "end":
        paths.append(path.copy())
    else:
        for edge in graph[node]:
            if edge not in explored:
                traverse(graph, edge, explored, path, paths)
    path.pop()
    if node in explored:
        del explored[node]


def main(input_file):
    graph = process_input(input_file)
    paths = []
    traverse(graph, node="start", explored={}, path=[], paths=paths)
    printer = PrettyPrinter()
    printer.pprint(paths)
    print(len(paths))


if __name__ == "__main__":
    main(sys.argv[1])
