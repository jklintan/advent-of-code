"""Solution to advent of code day 10 2022."""

import numpy as np


def main():
    """Main function for running day 10."""

    file_path = "input.txt"

    # Keep the current x value and current cycle in memory.
    # Save all crt values and register x for results.
    curr_val = 1
    current_cycle = 1
    crt = []
    register_x = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            current_input = line.strip().split(" ")
            command = current_input[0]
            
            # Noop represents one cycle.
            if command == "noop":
                register_x.append(curr_val)
                crt.append(get_pixel(current_cycle, curr_val))
                current_cycle = check_row_change(current_cycle + 1, 41)
                continue
            else:  
                # addx represents two cycles,
                # updates values after finished execution.

                # first cycle, starting the addx
                crt.append(get_pixel(current_cycle, curr_val))
                register_x.append(curr_val)
                current_cycle = check_row_change(current_cycle + 1, 41)

                # second cycle, executing the addx value
                crt.append(get_pixel(current_cycle, curr_val))
                curr_val += int(current_input[1])
                register_x.append(curr_val)
                current_cycle = check_row_change(current_cycle + 1, 41)

    # Part 1
    cycles_to_check = [20, 60, 100, 140, 180, 220]
    signal_strengths = [i * register_x[i-1] for i in cycles_to_check]
    print(sum(signal_strengths))

    # Part 2
    crt = np.array(crt).reshape(6, 40)
    for i in range(6):
        print("".join(crt[i, :]))


def check_row_change(index: int, max_row_val: int) -> int:
    """Checks if we have made a row change given max value of a row.

    Args:
        index (int): The current index.

    Returns:
        int: The next index to use.
    """
    # If max value, restart at 1.
    if index == max_row_val:
        return 1
    else:
        return index
    
def get_pixel(cycle: int, current_x_value: int) -> str:
    """Gets the pixel value for the current cycle, given the current x value.

    Args:
        cycle (int): Current cycle.
        current_x_value (int): Current x register value.

    Returns:
        str: "#" if the pixel is lit, "." otherwise.
    """
    sprite_position = [current_x_value, current_x_value + 1, current_x_value + 2]
    if cycle in sprite_position:
            return "#"
    else:
        return "."


if __name__ == '__main__':
    main()
