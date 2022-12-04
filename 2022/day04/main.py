"""Solution to advent of code day 4 2022."""


def main():
    """Main function for running day 4."""

    file_path = "input.txt"

    part_one_sum = 0
    part_two_sum = 0
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split(",")
            first0, first1 = row[0].split("-")
            second0, second1 = row[1].split("-")

            range1 = list(range(int(first0), int(first1) + 1))
            range2 = list(range(int(second0), int(second1) + 1))

            # Check if any of the ranges are a subset of the other.
            if (set(range1) <= set(range2)) or (set(range2) <= set(range1)):
                part_one_sum += 1

            # If the intersection between the ranges are non-empty,
            # they are overlapping.
            if (len(set(range1).intersection(range2)) > 0):
                part_two_sum += 1

    print(part_one_sum)
    print(part_two_sum)

if __name__ == '__main__':
    main()
