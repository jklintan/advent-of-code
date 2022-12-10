"""
Solution to advent of code day 9 2022.
A bit slow for the larger cases, but hey it works. :)
"""

import numpy as np


def main():
    """Main function for running day 9."""

    file_path = "input.txt"

    # Create a rather big map to make us not having
    # to check bounds every single iteration.
    height, width = 800, 800

    # A map with unique numbers on each vertices to help
    # us decide where we are on the map.
    help_map = np.array([range(height * width)]).reshape(height, width)

    # Start in the middle so we don't need to bother
    # about going out of range of the map.
    start = (int(height/2), int(width/2))

    # Keep track of which places that tail has visited.
    visited = np.zeros((height, width))

    # Part 1 = 2, part 2 = 10
    num_rope_parts = 10
    rope_parts = num_rope_parts * [start]

    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            input_sequence = line.strip().split(" ")
            direction = input_sequence[0]
            steps = int(input_sequence[1])
            for _ in range(steps):
                for i in range(num_rope_parts - 1):
                    curr_head = rope_parts[i]
                    curr_tail = rope_parts[i + 1]

                    # Only update the visited map if we are on
                    # the actual tail position.
                    if i == num_rope_parts - 2:
                        visited[curr_tail[0], curr_tail[1]] = 1

                    # Update head position in the right direction, only first head
                    # all others move according to it.
                    if i == 0:
                        if direction == "R":
                            curr_head = (curr_head[0], curr_head[1] + 1)
                        elif direction == "L":
                            curr_head = (curr_head[0], curr_head[1] - 1)
                        elif direction == "U":
                            curr_head = (curr_head[0] - 1, curr_head[1])
                        elif direction == "D":
                            curr_head = (curr_head[0] + 1, curr_head[1])

                        rope_parts[i] = curr_head

                    # 3x3 matrix centred around tail position.
                    surrounding_tail = help_map[curr_tail[0] - 1: curr_tail[0] + 2,
                                                curr_tail[1] - 1: curr_tail[1] + 2]
                    if curr_tail == curr_head or help_map[curr_head[0], curr_head[1]] in surrounding_tail:
                        # Head has not gone of further than closest
                        # neighborhood, we will not move tail in this case.
                        break
                    
                    # 3x3 matrix centred around head position.
                    surrounding_head = help_map[curr_head[0] - 1: curr_head[0] + 2,
                                                curr_head[1] - 1: curr_head[1] + 2]
                    four_neighbor = [
                        help_map[curr_head[0] - 1, curr_head[1]],
                        help_map[curr_head[0] + 1, curr_head[1]],
                        help_map[curr_head[0], curr_head[1] - 1],
                        help_map[curr_head[0], curr_head[1] + 1]
                    ]

                    # Check where we have overlapping spots (possible moving spaces).
                    set_head = set(surrounding_head.flatten())
                    set_tail = set(surrounding_tail.flatten())

                    possible_moves = set_head.intersection(set_tail)
                    indices = [np.where(help_map == i) for i in possible_moves]

                    # We will always get more at a minimum 2 overlaps, but
                    # we will always move tail to be non-diagonal to head.
                    if len(indices) == 1:
                        choice = possible_moves # Moving diagonally
                    else:
                        choice = [i for i in possible_moves if i in four_neighbor]
                        if len(choice) != 1:
                            print("We went out of range... increase map size")
                            return
                    indices = [np.where(help_map == i) for i in choice]
                    # We end up in list in tuple in set, weird indexing
                    curr_tail = (indices[0][0][0], indices[0][1][0])
                    rope_parts[i + 1] = curr_tail

                    # Ensure we visit the last position when no more lines to read
                    if i + 1 == num_rope_parts - 1:
                        visited[curr_tail[0], curr_tail[1]] = 1

    print(int(sum(sum(visited))))


if __name__ == '__main__':
    main()
