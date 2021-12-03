"""Day 1 solution for Advent of Code 2021"""

import sys
import numpy as np
from os import path
sys.path.append("../scripts/submarine")
from submarine import Submarine

def main() -> None:
    """Main function for day 1 solutions."""
    submarine = Submarine()
    print(submarine.sonar_sweep("input.txt"))  # Part 1
    print(submarine.sonar_sweep_sum("input.txt", 3))  # Part 2


if __name__ == '__main__':
    main()
