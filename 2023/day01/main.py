"""Solution to advent of code day 1 2023."""

import re
from typing import Tuple


def get_first_number(input: str) -> Tuple[str, int]:
    """Gets the first numeric in string and its index."""
    for i, ch in enumerate(input):
        if ch.isnumeric():
            return ch, i
    return "", -1


def get_last_number(input: str) -> Tuple[str, int]:
    """Gets the last numeric in string and its index."""
    reversed_input = input[::-1]
    for i, ch in enumerate(reversed_input):
        if ch.isnumeric():
            return ch, len(reversed_input) - i - 1
    return "", -1


def main():
    """Main function for running day 1."""

    file_path = "input.txt"
    part1_data = []
    part2_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            part1_data.append([item.strip("[\n]") for item in line])
            part2_data.append(line.strip("[\n]"))

    # Part 1
    answer_part_one = 0
    for line in part1_data:
        first, _ = get_first_number(line)
        last, _ = get_last_number(line)
        answer_part_one += int(first + last)

    print(f"Answer part 1 = {answer_part_one}")

    # Part 2
    numbers_as_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer_part_two = 0
    for line in part2_data:
        first, first_index = get_first_number(line)
        last, last_index = get_last_number(line)

        # Check if string representation exists.
        for i, num in enumerate(numbers_as_strings):
            # Check for one or many occurences of numbers in
            # the input data.
            indices = [
                match.start() for match in re.finditer(num, line)
            ]

            # No occurences found, nothing to do.
            if len(indices) == 0:
                continue

            # Check if any of the indices are lower or greater
            # than the previous found numeric version in the
            # input. In that case replace with the string version.
            for idx in indices:
                if idx < first_index or first_index == -1:
                    first_index = idx
                    first = str(i + 1)

                if idx > last_index or last_index == -1:
                    last_index = idx
                    last = str(i + 1)

        answer_part_two += int(first + last)

    print(f"Answer part 2 = {answer_part_two}")


if __name__ == '__main__':
    main()
