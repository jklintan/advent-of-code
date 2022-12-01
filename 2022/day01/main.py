"""Solution to advent of code day 1 2022.

Based on the bisect to not store any unnecessary sums
other than the number we are interested in. Works for
any number of length of toplist to keep.
"""

from typing import List
import bisect

def main():
    """Main function for running day 1."""

    top_list = get_top_list_elf_calories("input.txt", 3)

    # Part 1
    print(top_list[0])

    # Part 2
    print(sum(top_list))


def get_top_list_elf_calories(file_path: str, num_in_top: int) -> List[int]:
    """Gets a top list of a specified length of sum of calories each elf carries.

    Args:
        file_path (str): Path to puzzle input.
        num_in_top (int): Number of top sums to keep in toplist.

    Returns:
        List[int]: The toplist.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        running_sum = 0
        top_list = [0] * num_in_top
        for line in file:
            if not line.strip():
                bisect.insort(top_list, running_sum)
                top_list = top_list[1 : num_in_top + 1]
                running_sum = 0
                continue

            running_sum += int(line)

        # Check last element if no endline.
        if running_sum > top_list[0]:
            bisect.insort(top_list, running_sum)
            top_list = top_list[1 : num_in_top + 1]

    top_list.reverse()
    return top_list

if __name__ == '__main__':
    main()
