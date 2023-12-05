"""Solution to advent of code day 4 2023."""


def main():
    """Main function for running day 4."""

    file_path = "input.txt"
    winning_number_data = []
    my_numbers_data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        for row in file:
            input = row.split()
            split_index = input.index("|")
            winning_number_data.append(input[2:split_index])
            my_numbers_data.append(input[split_index + 1 :])

    points = 0
    copy_data = [1] * len(winning_number_data)
    for i, game in enumerate(winning_number_data):
        my_wins = [item for item in my_numbers_data[i] if item in game]
        num_winning_numbers = len(my_wins)

        # Check if we won this round, in that case
        # add the points and add the won copies for
        # part 2's scratchcard data.
        if num_winning_numbers > 0:
            points += pow(2, num_winning_numbers - 1)

            for j in range(i + 1, i + num_winning_numbers + 1):
                for _ in range(copy_data[i]):
                    copy_data[j] += 1

    print(f"Sum of winning game points = {points}")
    print(f"Number of scratchcards = {sum(copy_data)}")


if __name__ == "__main__":
    main()
