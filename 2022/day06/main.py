"""Solution to advent of code day 6 2022."""


def main():
    """Main function for running day 6."""

    # All input is in one line.
    file_path = "input.txt"
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            input_sequence = [item.strip("[\n]") for item in line]

    # stride = 4 for part 1, stride = 14 for part 2
    stride = 14
    index = 0
    count = stride
    while index + stride < len(input_sequence):
        unique_items = list(set(input_sequence[index:index+stride]))
        if len(unique_items) == stride:
            break
        count += 1
        index += 1

    print(count)


if __name__ == '__main__':
    main()
