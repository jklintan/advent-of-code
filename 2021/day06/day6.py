"""Solutions to day 6 of advent of code 2021."""

from typing import List
import numpy as np

def main() -> None:
    """Main function for day 6 solutions."""

    input_fishes = open("./input.txt").read().splitlines()[0].split(',')
    colony = LanternColony()
    for fish in input_fishes:
        colony.add_lantern_fish(int(fish))

    print(colony.advance_timer(256))  # Part 1 and 2


class LanternColony():
    """Class holding info about lantern fishes.

    Note that the naive solution of implementing this as
    an array that keeps holding separate information of all
    fishes in the colony would not work for part 2 where the
    number of fishes grows too large. Instead, we can store
    all info as number of fishes per time-span and limit the
    space to always be an array with fixed size of 9 entries.
    With this implementation, the calculation time is just
    around 1 second for 256 days time span.
    """

    def __init__(self) -> None:
        """Initializes a fish colony."""
        self.lantern_fishes: List[int] = np.zeros((9))
    
    def add_lantern_fish(self, timer: int) -> None:
        """Add a lantern fish to the colony."""
        self.lantern_fishes[timer] += 1

    def advance_timer(self, time_span: int) -> int:
        """Advance colony during a time span of x number of days."""
        for i in range(time_span):
            fishes_to_spawn = self.lantern_fishes[0]
            self.lantern_fishes[0] = 0
            self.lantern_fishes = shift(self.lantern_fishes, -1)
            self.lantern_fishes[8] = fishes_to_spawn
            self.lantern_fishes[6] += fishes_to_spawn
        return self.number_of_fishes()

    def number_of_fishes(self) -> int:
        """Gets the number of fishes currently in colony."""
        return int(np.sum(self.lantern_fishes))


def shift(arr: np.array, x: int) -> np.array:
    """Shifts an array x steps."""
    return np.roll(arr, x)

if __name__ == '__main__':
    main()