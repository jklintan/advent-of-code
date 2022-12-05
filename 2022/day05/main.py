"""Solution to advent of code day 5 2022."""


def main():
    """Main function for running day 5."""

    file_path = "input.txt"

    part_one, part_two = False, True
    top_crates = ""
    setup, init = False, False
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            line = [item.strip("[\n]") for item in line]

            # First line, initialize all columns as stacks.
            if not init:
                stacks = [[] for _ in range(len(line))]
                init = True

            # If we reach an empty line, we go between columns
            # and the instructions, make sure the stacks are
            # initialized as they should be.
            if len(line) == 1:
                stacks = [stack for stack in stacks if not len(stack) == 0]
                setup = True
                for i, item in enumerate(stacks):
                    item.reverse()
                continue

            # While not setup, add to the stacks.
            if not setup:
                for i, item in enumerate(line):
                    if item != " " and item != "" and not item.isdigit():
                        stacks[i].append(item)
                continue

            # Follow instructions, move from stack to stack,
            # part 1 simple pop and in part 2 we move them
            # as they are. We need to check if stacks are
            # empty and indices are correct.
            indices = [i for i in line if i.isdigit()]
            if len(indices) > 3:
                amount = int(indices[0] + indices[1])
            else:
                amount = int(indices[0])

            stack_from = int(indices[-2]) - 1
            stack_to = int(indices[-1]) - 1

            if part_one:
                for i in range(amount):
                    if len(stacks[stack_from]) > 0:
                        stacks[stack_to].append(stacks[stack_from].pop())

            if part_two:
                if amount > len(stacks[stack_from]):
                    amount = len(stacks[stack_from])

                to_move = []
                for i in range(amount):
                    to_move.append(stacks[stack_from].pop())

                to_move.reverse()
                for item in to_move:
                    stacks[stack_to].append(item)

    # Get output string.
    for _, item in enumerate(stacks):
        if len(item) > 0:
            top_crates += item.pop()

    print(top_crates)


if __name__ == '__main__':
    main()
