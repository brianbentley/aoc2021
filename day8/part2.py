"""Day 8 Part 1 of Advent of Code 2021"""
import sys


def process_input(input_file):
    display_signals = []
    with open(input_file, encoding="utf8") as input_data:
        current = input_data.readline()
        while current:
            display_signals.append([s.split() for s in current.split(" | ")])
            current = input_data.readline()
    return display_signals


def decode_wires(wire_input):
    wires = [set(w) for w in sorted(wire_input, key=lambda x: len(x))]
    one = wires[0]
    four = wires[2]
    seven = wires[1]
    eight = wires[9]

    five_segments = wires[3:6]
    six_segments = wires[6:9]

    for segment in six_segments:
        difference = segment - set.union(four, seven)
        if len(difference) == 1:
            nine = segment
    six_segments.remove(nine)
    for segment in six_segments:
        difference = segment - seven
        if len(difference) == 3:
            zero = segment
    six_segments.remove(zero)
    six = six_segments[0]

    for segment in five_segments:
        difference = segment - nine
        if len(difference) == 1:
            two = segment
    five_segments.remove(two)
    for segment in five_segments:
        difference = segment - one
        if len(difference) == 3:
            three = segment
    five_segments.remove(three)
    five = five_segments[0]

    wire_map = {
        "".join(sorted(one)): "1",
        "".join(sorted(two)): "2",
        "".join(sorted(three)): "3",
        "".join(sorted(four)): "4",
        "".join(sorted(five)): "5",
        "".join(sorted(six)): "6",
        "".join(sorted(seven)): "7",
        "".join(sorted(eight)): "8",
        "".join(sorted(nine)): "9",
        "".join(sorted(zero)): "0",
    }
    return wire_map


def main(input_file):
    display_signals = process_input(input_file)
    accumulator = 0
    for wire_input, display_output in display_signals:
        wire_map = decode_wires(wire_input)
        display_number = ""
        for number in display_output:
            number = "".join(sorted(list(number)))
            display_number += wire_map[number]
        accumulator += int(display_number)
    print(accumulator)


if __name__ == "__main__":
    main(sys.argv[1])
