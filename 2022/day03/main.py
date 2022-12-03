"""Solution to advent of code day 3 2022."""

import string


def main():
    """Main function for running day 3."""

    file_path = "input.txt"

    # Use indices of list for getting values of alphabetic chars.
    decoder = list(string.ascii_lowercase + string.ascii_uppercase)

    # Part 1, read one line at a time, split in half and then
    # get the intersection between them (as set), will be only
    # one single character, this we decode for the sum.
    part_one_sum = 0
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            row = line.strip()
            half = int(len(row)/2)
            first, second = row[:half], row[half:]
            twice_appearing_char = set(first).intersection(second)
            part_one_sum += decoder.index(twice_appearing_char.pop()) + 1

    print(part_one_sum)

    # Part 2, read 3 lines at a time, similary to the first part
    # we get the intersection of these three strings (as sets)
    # and decode the value of this character for the sum.
    part_two_sum = 0
    with open(file_path, mode='r', encoding='utf-8') as file:
        while True:
            line1 = file.readline().strip()
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            if not line3:
                break

            combined = set(line1).intersection(line2).intersection(line3)
            part_two_sum += decoder.index(combined.pop()) + 1

    print(part_two_sum)


if __name__ == '__main__':
    main()
