"""Solutions to day 3 of advent of code 2021."""

import numpy as np


def main() -> None:
    """Main function for day 3 solutions."""
    power_consumption_data = get_power_data("./input.txt")
    print(calculate_power_consumption(power_consumption_data))  # Part 1
    print(calculate_life_support_rating(power_consumption_data, "./input.txt"))  # Part 2


def get_power_data(report: str) -> np.array:
    """Gets the power data as an array of counted occurences of bits in report.

    Args:
        report (str): File to parse bit-data from.

    Returns:
        np.array: Array of counted occurences of 0's and 1's.
    """
    with open(report, mode='r', encoding='utf-8') as file:
        line = file.readline().strip()
        power_data = np.repeat([[0], [0]], len(line), axis = 1)
        while line:
            for i, char in enumerate(line):
                power_data[int(char), i] += 1
            line = file.readline().strip()

    return power_data


def calculate_power_consumption(power_data: np.array) -> int:
    """Calculates the power consumption for a submarine.

    Power consumption = gamma_rate * epsilon_rate.

    Args:
        power_data (np.array):

    Returns:
        int: The power consumption.
    """
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(power_data.shape[1]):
        gamma_rate += '0' if power_data[0, i] >= power_data[1, i] else '1'
        epsilon_rate += '0' if power_data[0, i] <= power_data[1, i] else '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_rating(power_data: np.array, report: str, rating_type: str) -> int:
    """Calculates the oxygen rating and C02 scrubber rating.

    The oxygen rating is calculated when we consider the most
    occuring bit per char in the input in the report. The C02 rating
    is calculated when we consider the least occuring bit per char in
    the input numbers in the report.

    Args:
        power_data (np.array): Number of occurences of bits in report.
        report (str): Path to report.
        rating_type (str): "oxygen" or "c02".

    Raises:
        ValueError: If the rating_type is neither "oxygen" or "c02".

    Returns:
        int: The oxygen rating or C02 scrubber rating in decimal.
    """
    to_keep = []
    with open(report, mode='r', encoding='utf-8') as file:
        line = file.readline().strip()
        while line:
            if rating_type == "c02":
                val = '1' if power_data[1, 0] < power_data[0, 0] else '0'
            elif rating_type == "oxygen":
                val = '1' if power_data[1, 0] >= power_data[0, 0] else '0'
            else:
                raise ValueError("ERROR: Invalid rating type!")

            if line[0] == val:
                to_keep.append(line)
       
            line = file.readline().strip()

    index = 1
    while len(to_keep) > 1 and index < len(to_keep[0]):
        zeros = [item for item in to_keep if item[index] == '0']
        ones = [item for item in to_keep if item[index] == '1']
        if rating_type == "c02":
            if len(ones) < len(zeros):
                to_keep = [number for number in to_keep if number not in zeros]
            else:
                to_keep = [number for number in to_keep if number not in ones]
        elif rating_type == "oxygen":
            if len(ones) >= len(zeros):
                to_keep = [number for number in to_keep if number not in zeros]
            else:
                to_keep = [number for number in to_keep if number not in ones]
        else:
            raise ValueError("ERROR: Invalid rating type!")

        index += 1

    return int(to_keep[0], 2)


def calculate_life_support_rating(power_data: np.array, report: str) -> int:
    """Calculates the life support rating.

    life_support_rating = oxygen_generator_rating * C02_scrubber_rating

    Args:
        power_data (np.array): Number of occurences of bits in report.
        report (str): Path to report.

    Returns:
        int: The life support rating in decimal.
    """
    return (calculate_rating(power_data, report, "oxygen")
    * calculate_rating(power_data, report, "c02"))


if __name__ == '__main__':
    main()
