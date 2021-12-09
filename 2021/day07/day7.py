"""Solutions to day 7 of advent of code 2021."""

import numpy as np

def main() -> None:
    """Main function for day 7 solutions."""

    input_data = open("./input.txt").read().splitlines()[0].split(',')
    input_vec = np.array([int(x) for x in input_data])
    mean_val = np.mean(input_vec)

    best = -1
    for i in range(int(mean_val/2), int(mean_val) + 1):  # Optimal value should be around mean
        cost = 0
        for k in range(input_vec.shape[0]):
            # cost += np.abs(input_vec[k] - i)  # Part 1
            cost += np.sum(list(range(np.abs(input_vec[k] - i) + 1)))  # Part 2

        if cost < best or best < 0:
            best = cost
        
        cost = 0

    print(best)


if __name__ == '__main__':
    main()