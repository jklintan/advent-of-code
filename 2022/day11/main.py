"""Solution to advent of code day 11 2022."""

import operator
from typing import List


def main():
    """Main function for running day 11."""

    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }
    file_path = "input.txt"

    # Parse the input once and save everything we need for
    # calculating the worry levels further on.
    new_monkey_input = True
    num_monkeys = 8
    monkeys_items =  [ [] for _ in range(num_monkeys) ]
    monkey_activity = [0] * num_monkeys
    monkey_operations = [""] * num_monkeys
    monkey_terms = [""] * num_monkeys
    monkey_division = [0] * num_monkeys
    throws_to = [ [0, 0] for _ in range(num_monkeys) ]

    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
           
            if line.strip() == "":
                new_monkey_input = True
                continue
        
            current_line = line.strip().split(" ")
            if new_monkey_input:
                current_monkey = int(current_line[-1].split(":")[0])

                # items
                line = file.readline().strip().split(":")
                holds_items = line[-1].strip().split(", ")
                holds_items = [int(i) for i in holds_items]
                for item in holds_items:
                    monkeys_items[current_monkey].append(item)

                # operation
                line = file.readline().strip().split(" ")
                operation = line[-2]
                monkey_operations[current_monkey] = operation
                term = line[-1]
                monkey_terms[current_monkey] = term

                # test
                line = file.readline().strip().split(" ")
                div_by = int(line[-1])
                monkey_division[current_monkey] = div_by

                # if true
                line = file.readline().strip().split(" ")
                if_true_throw_to = int(line[-1])
                throws_to[current_monkey][0] = if_true_throw_to

                # if false
                line = file.readline().strip().split(" ")
                if_false_throw_to = int(line[-1])
                throws_to[current_monkey][1] = if_false_throw_to

                new_monkey_input = False

    # Find the least common multiplier of division numbers, for part 2.
    lcm = get_smallest_number_satisfying_modulus(monkey_division)
    
    # Part 1, num_rounds = 20. Part 2, num_rounds = 10000
    num_rounds = 10000
    for i in range(num_rounds):
        for j in range(num_monkeys):
            current_monkey =j
            curr_items = monkeys_items[current_monkey]

            if len(curr_items) == 0:
                continue

            # operation
            operation = monkey_operations[current_monkey]
            term = monkey_terms[current_monkey]

            # test
            div_by = monkey_division[current_monkey]

            # if true
            if_true_throw_to = throws_to[current_monkey][0]

            # if false
            if_false_throw_to = throws_to[current_monkey][1]

            for _ in range(len(curr_items)):                
                item = curr_items.pop(0)
                monkey_activity[current_monkey] += 1

                if term == "old":
                    worry_level = ops[operation](item, item)
                else:
                    worry_level = ops[operation](item, int(term))

                # For part 1
                # worry_level = ops["/"](worry_level, 3)

                # For part 2
                # keeping the worry level from growing too large.
                worry_level = worry_level % lcm

                if worry_level % div_by == 0:
                    monkeys_items[if_true_throw_to].append(worry_level)
                else:
                    monkeys_items[if_false_throw_to].append(worry_level)

    monkey_activity.sort(reverse=True)
    print(monkey_activity[0] * monkey_activity[1])


# Finds the L.C.M
def get_smallest_number_satisfying_modulus(divs: List[int]):
    """Finds the least common multiple of a list of integers.

    Args:
        divs (List[int]): List of integers.

    Returns:
        int: The smallest number that is a multiple of all numbers in divs.
    """
    n = min(divs)
    while True:
        if sum([n % i for i in divs]) == 0:
            return n
        n += 1


if __name__ == '__main__':
    main()
