"""Submarine class."""

import numpy as np


class Submarine:
    """Submarine class.
    
    Attributes:
        current_depth (int): Depth below the surface, positive.
        horizontal_position (int): Current position.
    """
    def __init__(self) -> None:
        """Initialization of submarine class."""
        self._current_depth = 0
        self._horizontal_position = 0
        self._aim = 0

    @property
    def current_depth(self) -> int:
        """Gets the current depth."""
        return self._current_depth

    @property
    def horizontal_position(self) -> int:
        """Gets the current horizontla position."""
        return self._horizontal_position

    def submerge(self) -> None:
        """Re-enters the submarine to start."""
        self._current_depth = 0
        self._depth_sum = 0
        self._horizontal_position = 0
        self._aim = 0

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
                    self._current_depth = int(line)
                    init = True
                else:
                    if int(line) > self._current_depth:
                        count += 1
                self._current_depth = int(line)
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
        depth_sum = np.sum(vals[:n_vals])
        while i + n_vals < len(vals) + 1:
            curr_depth_sum = np.sum(vals[i: i+3])
            if curr_depth_sum > depth_sum:
                count += 1
            depth_sum = curr_depth_sum
            i += 1

        return count

    def move(self, move_report: str, use_aim: bool = False) -> None:
        """Moves the submarine according to input file.
        
        Args:
            move_report (str): Path to input file.
            use_aim (bool): If we use aim to calculate the
                depth or simply the input file. Defaults to False.
        """
        with open(move_report) as file:
            line = file.readline()
            while line:
                cmds = line.split()
                direction = cmds[0].lower()
                amount = int(cmds[1])
                if direction == "forward":
                    self._horizontal_position += amount
                    if use_aim and self._aim != 0:
                        self._current_depth += (self._aim * amount)
                elif direction == "up":
                    if use_aim:
                        self._aim -= amount
                    else:
                        self._current_depth -= amount
                elif direction == "down":
                    if use_aim:
                        self._aim += amount
                    else:
                        self._current_depth += amount
                line = file.readline()
