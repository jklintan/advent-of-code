"""Solution to advent of code day 3 2023."""

import numpy as np


def find_num_non_forbidden_adjacent_elements(
    i, j, data, directions, forbidden_elements
):
    """Check in given directions from an index to see if we
    find data that is not in the forbidden elements. Give back
    the number of adjacent elements fulfilling this criteria.
    """
    result = 0
    for direction in directions:
        try:
            adjacent_element = data[i + direction[0]][j + direction[1]]
            if adjacent_element not in forbidden_elements:
                result += 1
        except IndexError:
            pass
    return result


def find_adjacent_element(i, j, data, directions, element):
    """Check in given directions from an index to see if we
    find any data entry equal to element. Give back the
    indices of the found elements."""
    elements = []
    for direction in directions:
        try:
            adjacent_element = data[i + direction[0]][j + direction[1]]
            if adjacent_element == element:
                elements.append([i + direction[0], j + direction[1]])
        except IndexError:
            pass
    return elements


def get_number_existing_on_index(i, j, num_data, symbol_data):
    """Get number representation from a given index.
    This number may span over multiple indices."""
    numb = str(num_data[i][j])
    idy = j - 1
    if idy > 0:
        while idy != -1:
            if symbol_data[i][idy] != "n":
                break
            numb = str(num_data[i][idy]) + numb
            idy -= 1
    idy = j + 1
    if idy < len(num_data[0]):
        while idy != len(num_data[0]):
            if symbol_data[i][idy] != "n":
                break
            numb += str(num_data[i][idy])
            idy += 1

    return int(numb)


def get_directions_for_index(i, j, max_i, max_j):
    """Gets the possible directions to step in from
    a given index. We allow 8 different steps for any
    mid-matrix element and removes invalid steps if we
    have an index on the border of the matrix.
    """
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
    if i == 0:
        directions.remove([-1, 0])
        directions.remove([-1, -1])
        directions.remove([-1, 1])
    if i == max_i:
        directions.remove([1, 0])
        directions.remove([1, -1])
        directions.remove([1, 1])
    if j == 0:
        directions.remove([0, -1])
        directions.remove([-1, -1])
        directions.remove([1, -1])
    if j == max_j:
        directions.remove([0, 1])
        directions.remove([-1, 1])
        directions.remove([1, 1])

    return directions


def main():
    """Main function for running day 3."""

    # Read input data, keep 2 matrices, one that is storing
    # the actual input and one that is signalling if number
    # entry of if symbol entry.
    file_path = "input.txt"
    symbol_data = []
    num_data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        for row in file:
            row_data = []
            num_row_data = []
            for item in row:
                i = item.strip()
                if i == "":
                    continue
                num_row_data.append(i)
                if i.isdigit():
                    row_data.append("n")
                else:
                    row_data.append(i)
            num_data.append(num_row_data)
            symbol_data.append(row_data)

    symbol_data = np.array(symbol_data)
    max_row = len(symbol_data)
    max_col = len(symbol_data[0])

    part1 = 0
    part2 = 0

    # Flags for keeping track of data handling for part 1.
    part_number = False
    is_new_number = True
    current_number = ""

    for i, row in enumerate(symbol_data):
        for j, _ in enumerate(row):
            # Part 1, check if the input is a digit, and if so
            # keep track if it is part of a current number or
            # start of a new one. As soon as we meet a non-digit
            # we reset the number and check if it is a part number
            # that should be added to the sum.
            if symbol_data[i][j] == "n":
                if is_new_number:
                    current_number = ""
                    is_new_number = False
                directions = get_directions_for_index(i, j, max_row, max_col)
                found_adjacent = find_num_non_forbidden_adjacent_elements(
                    i, j, symbol_data, directions, ["n", "."]
                )

                # If we found that the digit has ana djacent
                # symbol, it is a part number.
                if found_adjacent > 0:
                    part_number = True

                current_number += num_data[i][j]
            else:
                # We have now finished the current
                # number, and if any of its digits
                # was adjacent to a symbol, it was
                # flagged as a part number and added
                # to the output sum. Reset flags.
                if part_number:
                    part1 += int(current_number)
                part_number = False
                current_number = ""
                is_new_number = True

            # Part 2, look specifically for the "*".
            if symbol_data[i][j] == "*":
                directions = get_directions_for_index(i, j, max_row, max_col)
                adjacent = find_adjacent_element(i, j, symbol_data, directions, "n")

                # Check all "*" that has at least 2 adjacent
                # numbers. It might have duplicates of the same
                # or more than 2 numbers. We will sort out so
                # only the ones with exactly 2 unique ones will
                # be added for the gear ratio.
                if len(adjacent) > 1:
                    gear_nums = []
                    for a in adjacent:
                        num = get_number_existing_on_index(
                            a[0], a[1], num_data, symbol_data
                        )

                        # Assumption of non-equal pairs.
                        if num not in gear_nums:
                            gear_nums.append(num)

                    if len(gear_nums) == 2:
                        part2 += gear_nums[0] * gear_nums[1]

    print(f"Sum of the part numbers = {part1}")
    print(f"Sum of all gear ratios = {part2}")


if __name__ == "__main__":
    main()
