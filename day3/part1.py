"""Day 3 Part 1 of Advent of Code 2021"""
import sys


def calculate_gamma(binary_map):
    gamma = [None] * len(binary_map.keys())
    for k, v in binary_map.items():
        ones = v[1]
        zeros = v[0]
        if ones > zeros:
            gamma[k] = "1"
        else:
            gamma[k] = "0"
    return "0b" + "".join(gamma)


def calculate_epsilon(binary_map):
    epsilon = [None] * len(binary_map.keys())
    for k, v in binary_map.items():
        ones = v[1]
        zeros = v[0]
        if ones > zeros:
            epsilon[k] = "0"
        else:
            epsilon[k] = "1"
    return "0b" + "".join(epsilon)


def main(input_file):
    """Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
    then multiply them together. What is the power consumption of the submarine?"""
    binary_map = {}
    with open(input_file, encoding="utf8") as input:
        first_run = True
        current = input.readline().strip()
        while current:
            if first_run:
                first_run = False
                for i, v in enumerate(current):
                    binary_map[i] = {0: 0, 1: 0}
            for i, v in enumerate(current):
                if v == "1":
                    binary_map[i][1] += 1
                else:
                    binary_map[i][0] += 1
            current = input.readline().strip()
    gamma = calculate_gamma(binary_map)
    epsilon = calculate_epsilon(binary_map)
    print(binary_map)
    print(f"gamma: {gamma}")
    print(f"gamma(int): {int(gamma, 2)}")
    print(f"epsilon: {epsilon}")
    print(f"epsilon(int): {int(epsilon, 2)}")
    print(f"power consumption: {int(epsilon, 2) * int(gamma, 2)}")


if __name__ == "__main__":
    main(sys.argv[1])
