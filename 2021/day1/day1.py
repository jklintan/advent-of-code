"""Day 1 solution for Advent of Code 2021"""

import numpy as np


class Submarine():
    """Submarine class.
    
    Attributes:
        current_depth (int): Depth below the surface, positive.
        depth_sum (int): Current depth sum, average.
    """
    def __init__(self) -> None:
        """Initialization of submarine class."""
        self.current_depth = 0
        self.depth_sum = 0

    def sonar_sweep(self, report: str) -> int:
        """Sonar sweep and calculate the number of increased depth measures.
        
        Note, no notice is taken of cases such as empty report-files or
        other potential errors while parsing.

        Args:
            report (str): Path to depth report.

        Returns:
            int: The number of increased depth values in the report.
        """
        count = 0
        init = False
        with open(report) as file:
            line = file.readline()
            while line:
                if not init:
                    self.current_depth = int(line)
                    init = True
                else:
                    if int(line) > self.current_depth:
                        count += 1
                self.current_depth = int(line)
                line = file.readline()

        return count

    def sonar_sweep_sum(self, report: str, n_vals: int) -> int:
        """Sonar sweep and calculate the number of increased depth values as sum.
        
        Calculate the depth from a report-file and measure the depth
        as a sum of a number of values.

        Note, no notice is taken of cases such as empty report-files or
        other potential errors while parsing.
        
        Args:
            report (str): Path to depth report.
            n_vals (int): Number of values to add.

        Returns:
            int: The number of increased depth values in the report.
        """

        # Read in all values for summation.
        vals = []
        with open(report) as file:
            line = file.readline()
            while line:
                vals.append(int(line))
                line = file.readline()

        vals = np.array(vals)

        i = 1
        count = 0
        self.depth_sum = np.sum(vals[:n_vals])
        while i + n_vals < len(vals) + 1:
            curr_depth_sum = np.sum(vals[i: i+3])
            if curr_depth_sum > self.depth_sum:
                count += 1
            self.depth_sum = curr_depth_sum
            i += 1

        return count


submarine = Submarine()
print(submarine.sonar_sweep("input.txt"))  # Part 1
print(submarine.sonar_sweep_sum("input.txt", 3))  # Part 2
