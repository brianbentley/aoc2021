"""Day 4 Part 1 of Advent of Code 2021"""
import sys


class BingoBoard:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers
        self.played_numbers = []
        self.board_state = []
        self.row_count = len(self.numbers)
        for row in range(self.row_count):
            self.board_state.append([0] * self.row_count)

    def play_number(self, number):
        self.played_numbers.append(number)
        for i in range(self.row_count):
            for j in range(self.row_count):
                if self.numbers[i][j] == number:
                    self.board_state[i][j] = 1
        return self.check_bingo()

    def check_bingo(self):
        for row in self.board_state:
            if sum(row) == self.row_count:
                return True
        for i in range(self.row_count):
            if sum([r[i] for r in self.board_state]) == self.row_count:
                return True
        return False

    def score(self):
        accumulator = 0
        for i in range(self.row_count):
            for j in range(self.row_count):
                if self.board_state[i][j] == 0:
                    accumulator += self.numbers[i][j]
        return accumulator * self.played_numbers[-1]

    def __str__(self):
        return "\n".join([f"board: {self.name}"] + [str(n) for n in self.numbers])


def process_input(input_file):
    with open(input_file, encoding="utf8") as input_data:
        numbers = [int(x.strip()) for x in input_data.readline().split(",")]
        boards = []
        new_line = input_data.readline()
        current_board = []
        while new_line:
            bingo_line = [int(x) for x in new_line.split()]
            if bingo_line:
                current_board.append(bingo_line)
            else:
                if current_board:
                    boards.append(current_board)
                current_board = []
            new_line = input_data.readline()
        boards.append(current_board)
    board_map = {}
    for i, board in enumerate(boards):
        board_map[f"board {i + 1}"] = BingoBoard(f"board {i + 1}", board)

    return numbers, board_map


def main(input_file):
    """The submarine has a bingo subsystem to help passengers (currently,
    you and the giant squid) pass the time.
    It automatically generates a random order in which to draw numbers
    and a random set of boards (your puzzle input)."""
    numbers, boards = process_input(input_file)
    rounds = []
    print(f"numbers: {numbers}")
    winner = False
    for number in numbers:
        print(f"playing number: {number}")
        round = {}
        for board in boards.values():
            round[board.name] = board.play_number(number)
        rounds.append(round)
        for board, result in round.items():
            if result == True:
                print(f"{board} is the winner")
                print(f"score: {boards[board].score()}")
                winner = True
        if winner:
            break


if __name__ == "__main__":
    main(sys.argv[1])
