"""Solution to advent of code day 8 2022."""

import numpy as np


def main():
    """Main function for running day 8."""

    # Read in the forest map
    file_path = "input.txt"
    forest_map = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            forest_map.append(list(line.strip()))

    forest_map = np.array(forest_map)
    visibility_map = np.zeros((forest_map.shape))

    # Move over grid from left to right and
    # check which trees are visible from border.
    width, height = forest_map.shape
    visibility_map = np.zeros((forest_map.shape))
    for x in range(height):
        for y in range(width):
            up = is_tree_visible(x, y, "-x", forest_map)
            down = is_tree_visible(x, y, "x", forest_map)
            left = is_tree_visible(x, y,"-y", forest_map)
            right = is_tree_visible(x, y, "y", forest_map)
            if up or down or left or right:
                visibility_map[x, y] = 1

    # Part 1 - sums up the number of visible trees.
    num_visible_trees = int(sum(sum(visibility_map)))
    print(num_visible_trees)

    # Part 2 - gets the scenic scores for all trees
    # to get the one with maximum score.
    scores = np.zeros((forest_map.shape))
    for x in range(height):
        for y in range(width):
            if is_tree_on_edge(x, y, forest_map):
                continue

            scores[x, y] = get_scenic_score_for_tree(x, y, forest_map)

    maximal_score = int(scores.max())
    print(maximal_score)


def is_tree_visible(x: int, y: int, direction: str, forest_map: np.ndarray) -> bool:
    """Checks if a tree is visible from a border given a direction.

    Args:
        x (int): Current x position of the tree.
        y (int): Current y position of the tree.
        direction (str): Direction to test.
        forest_map (np.ndarray): The forest map of all trees.

    Returns:
        bool: True if the tree is visible, False otherwise.
    """
    val = forest_map[x, y]
    width, height = forest_map.shape
    is_visible = True
    if direction == "-x":
        check = [i for i in forest_map[:x, y] if i < val]
        is_visible = True if len(check) == x else False
    elif direction == "x":
        check = [i for i in forest_map[x:, y] if i < val]
        is_visible = True if len(check) == (width - 1 - x) else False
    elif direction == "-y":
        check = [i for i in forest_map[x, :y] if i < val]
        is_visible = True if len(check) == y else False
    elif direction == "y":
        check = [i for i in forest_map[x, y:] if i < val]
        is_visible = True if len(check) == (height - 1 - y) else False

    return is_visible


def is_tree_on_edge(x: int, y: int, forest_map: np.ndarray) -> bool:
    """Checks if a coordinate is on the edge of the map or not.

    Args:
        x (int): Current x position of the tree.
        y (int): Current y position of the tree.
        forest_map (np.ndarray): The forest map of all trees.

    Returns:
        bool: True if the tree is on the edge, False otherwise.
    """
    dimx, dimy = forest_map.shape
    return x == 0 or x == dimx - 1 or y == 0 or y == dimy - 1


def get_scenic_score_for_tree(x: int, y: int, forest_map: np.ndarray):
    """Gets the scenic score for the current tree.

    Args:
        x (int): Current x position of the tree.
        y (int): Current y position of the tree.
        forest_map (np.ndarray): The forest map of all trees.

    Returns:
        int: The scenic score of the tree = vis_left * vis_right * vis_up * vis_down.
    """
    height_of_tree = forest_map[x, y]

    # go up
    curr_x = x
    visible_up = 0
    while not curr_x == 0:
        curr_x = curr_x - 1
        visible_up += 1
        # We stop on the edge or if we see a tree higher than the one we are in.
        if is_tree_on_edge(curr_x, y, forest_map) or forest_map[curr_x, y] >= height_of_tree:
            break

    # go down
    curr_x = x
    visible_down = 0
    while True:
        curr_x = curr_x + 1
        visible_down += 1
        # We stop on the edge or if we see a tree higher than the one we are in.
        if is_tree_on_edge(curr_x, y, forest_map) or forest_map[curr_x, y] >= height_of_tree:
            break

    # go left
    curr_y = y
    visible_left = 0
    while True:
        curr_y = curr_y - 1
        visible_left += 1
        # We stop on the edge or if we see a tree higher than the one we are in.
        if is_tree_on_edge(x, curr_y, forest_map) or forest_map[x, curr_y] >= height_of_tree:
            break

    # go right
    curr_y = y
    visible_right = 0
    while True:
        curr_y = curr_y + 1
        visible_right += 1
        # We stop on the edge or if we see a tree higher than the one we are in.
        if is_tree_on_edge(x, curr_y, forest_map) or forest_map[x, curr_y] >= height_of_tree:
            break

    return visible_up * visible_down * visible_left * visible_right


if __name__ == '__main__':
    main()
