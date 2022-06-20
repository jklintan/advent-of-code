"""Day 8 solution for Advent of Code 2021"""

from typing import List, Tuple

def main() -> None:
    """Main function for day 8 solutions."""

    # Read input and output.
    input_sequences, output_sequences = read_input_file("input.txt")

    # Part 1
    output_sum = 0
    for sequence in output_sequences:
        for item in sequence:
            word_length = len(item)
            if word_length in (2, 3, 4, 7):
                output_sum += 1

    print(f"The answer to part 1 = {output_sum}")

    # Part 2
    # Decoder represents the number output according to indices:
    #
    #       000
    #      1   2
    #      1   2
    #       333
    #      4   5
    #      4   5
    #       666
    #
    decoder = [""] * 7
    output_sum = 0
    for index, sequence in enumerate(input_sequences):
        # Storage of which character sequence that represent
        # each number [0, 9], represented by its index.
        decoded_values = [""] * 10

        # Get the items of known size, 1, 4, 7, 8.
        # We know it will be only one item of each size for them.
        decoded_values[1] = get_words_by_length(sequence, 2)[0]
        decoded_values[4] = get_words_by_length(sequence, 4)[0]
        decoded_values[7] = get_words_by_length(sequence, 3)[0]
        decoded_values[8] = get_words_by_length(sequence, 7)[0]

        # Get the top character on index 0 in the decoder,
        # found by getting the third character in number
        # 7, the one that do not occurr in number 1.
        decoder[0] = [char for char in decoded_values[7] if char not in decoded_values[1]][0]

        # Now we have the 6 unkown, 3 of length 6 and 3 of length 5.
        unknown_len6 = get_words_by_length(sequence, 6)
        unknown_len5 = get_words_by_length(sequence, 5)

        # We can find the number 9 by getting the word of length 6 that
        # contain the top char and all the chars in the number 4.
        decoded_values[9], decoder[6] = get_missing_word_and_char(
            unknown_len6, list(decoded_values[4] + decoder[0])
        )
        unknown_len6.remove(decoded_values[9])

        # We can find the number 3 by getting the word of length 5 that
        # contain the top & bottom char and all the chars in the number 1.
        decoded_values[3], decoder[3] = get_missing_word_and_char(
            unknown_len5, list(decoder[0] + decoder[6] + decoded_values[1])
        )
        unknown_len5.remove(decoded_values[3])

        # Get the last char from the number 9 that are not
        # already known, this should be on index 1 in decoder.
        for char in decoded_values[9]:
            if not (char == decoder[0] or
                    char == decoder[3] or
                    char == decoder[6] or
                    char in decoded_values[1]
                ):
                decoder[1] = char

        # The zero is distinguished from number 6 by not having decoder[3] in it.
        decoded_values[0] = [unknown for unknown in unknown_len6 if decoder[3] not in unknown][0]
        unknown_len6.remove(decoded_values[0])

        # The value 6 is the last char of lenght 6 left at this stage.
        decoded_values[6] = unknown_len6[0]

        # The 5 is distinguished from 2 by having decoder value 0, 1, 3 and 6 in it.
        for unknown in unknown_len5:
            if (decoder[0] in unknown and
                decoder[1] in unknown and
                decoder[3] in unknown and
                decoder[6] in unknown
            ):
                decoded_values[5] = unknown
                unknown_len5.remove(unknown)
                break

        # The value 2 is the last unknown of length 5.
        decoded_values[2] = unknown_len5[0]

        # Sort the decoded values in alphabetical order to ensure
        # that we can encode all the output values which may contain
        # the chars in a different order.
        decoded_values = sort_internal_items_alphabetically(decoded_values)

        # Decode the output values.
        output_value = ""
        for item in output_sequences[index]:
            output_numb = "".join(sorted(item))
            output_value += str(decoded_values.index(output_numb))

        output_sum += int(output_value)

    print(f"The answer to part 2 = {output_sum}")


def get_missing_word_and_char(words: List[str], characters: List[str]) -> Tuple[str, str]:
    """Gets the word from a list that contains all chars but one in a list of characters.

    Args:
        words (List[str]): List of words to check.
        characters (List[str]): List of chars that should appear.

    Returns:
        Tuple[str, str]: The word (if found) and the extra char appearing in it.
    """
    for word in words:
        missing = 0
        for char in word:
            if not char in characters:
                missing += 1
                if missing > 1:  # Not the one we are looking for
                    break
                missing_char = char

        if missing == 1:
            return word, missing_char
        missing = 0

    return "", ""


def get_words_by_length(words: List[str], length: int) -> List[str]:
    """Gets word from a list of a certain length.

    Args:
        sequence (List[str]): List of words.
        length (int): Length to choose.

    Returns:
        List[str]: A list of all words in the input list that has the given length. 
    """
    return [item for item in words if len(item) == length]


def sort_internal_items_alphabetically(list_to_sort: List[str]) -> List[str]:
    """Sorts the words in a list alphabetically.

    Args:
        list_to_sort (List[str]): The list to sort.

    Returns:
        List[str]: The sorted list.
    """
    for i, item in enumerate(list_to_sort):
        list_to_sort[i] = "".join(sorted(item))

    return list_to_sort


def read_input_file(file_path: str) -> Tuple[List[str], List[str]]:
    """Reads input and output sequences to decode from an input file.

    It reads the file and sets all words before the character "|" to be
    input values, and all after the next character "|" to be output values.

    Args:
        file_path (str): Path to the input file.

    Returns:
        Tuple[List[str], List[str]]: List of input sequences and list of
            output sequences.
    """
    input_sequences = []
    output_sequences = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        line = file.readline().strip()
        while line:
            numbers = line.split(" ")
            i = numbers.index("|")
            input_numbers = numbers[:i]
            output_numbers = numbers[i+1:]
            line = file.readline().strip()
            input_sequences.append(input_numbers)
            output_sequences.append(output_numbers)

    return input_sequences, output_sequences


if __name__ == '__main__':
    main()
