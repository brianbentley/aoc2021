"""Day 12 Part 2 of Advent of Code2021"""
import sys
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


def path_filter(node, path):
    initial_filter = node.isupper() or node not in path
    small_caves = [n for n in path if n.islower()]
    is_small_duplicate = len(small_caves) == len(set(small_caves))
    return initial_filter or (is_small_duplicate and node not in ["start", "end"])


def traverse(graph, node, path, paths):
    path.append(node)
    if node == "end":
        paths.append(path.copy())
    else:
        for edge in graph[node]:
            if path_filter(edge, path):
                traverse(graph, edge, path, paths)
    path.pop()


def main(input_file):
    graph = process_input(input_file)
    paths = []
    traverse(graph, node="start", path=[], paths=paths)
    if "test" in input_file:
        printer = PrettyPrinter()
        printer.pprint(paths)
    print(len(paths))


if __name__ == "__main__":
    main(sys.argv[1])
