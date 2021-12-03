"""Solutions to day 2 of advent of code 2021."""

import sys
from os import path
sys.path.append("../scripts/submarine")
from submarine import Submarine

def main() -> None:
    """Main function for day 2 solutions."""
    submarine = Submarine()
    submarine.move("./input.txt")
    print(submarine.horizontal_position * submarine.current_depth)  # Part 1

    # Reset submarine for second part.
    submarine.submerge()
    submarine.move("./input.txt", use_aim = True)
    print(submarine.horizontal_position * submarine.current_depth)  # Part 2


if __name__ == '__main__':
    main()