"""Solution to advent of code day 7 2022."""

import os
import shutil


def main():
    """Main function for running day 7."""

    # All input is in one line.
    file_path = "input.txt"
    curr_dir = "out"
    os.mkdir(curr_dir)
    # Builds the specified folder hierarchy from input
    # in a dummy folder called /out in the current dir.
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            command = line.strip()
            if "$" in command:
                if "cd" in command:
                    if ".." in command:
                        curr_dir = curr_dir.split("/")
                        curr_dir = "/".join(curr_dir[:-1])
                        continue

                    curr = command.split(" ")
                    if curr[-1] == "/":
                        continue
                    curr_dir = f"{curr_dir}/{curr[-1]}"
                    if not os.path.exists(f"{curr_dir}"):
                        os.mkdir(f"{curr_dir}")
            elif "dir" in command:
                curr = command.split(" ")[-1]
                os.mkdir(f"{curr_dir}/{curr}")
            else:
                curr = command.split(" ")[0]
                if not os.path.exists(f"{curr_dir}/{curr}.txt"):
                    # Dummy empty file, name is the size of it.
                    open(f"{curr_dir}/{curr}.txt", 'w').close()

    # Recursively visit all folders and count their sizes.
    top_dir = "./out"
    dirs = [top_dir]
    result = []
    while len(dirs) > 0:
        curr = dirs.pop()
        result.append(get_folder_size(curr))
        subdirs = [f for f in os.listdir(curr) if os.path.isdir(f"{curr}/{f}")]
        for directory in subdirs:
            dirs.append(f"{curr}/{directory}")

    # Part 1, sum up all folders with size under 100000.
    res = [i for i in result if i < 100000]
    print(sum(res))

    # Part 2, find a directory to delete to free up space.
    total_space = 70000000
    update_memory_required = 30000000
    largest_folder = sorted(result)[-1]
    unused_space = total_space - largest_folder
    need_to_free = update_memory_required - unused_space

    # Find the smallest directory size which we can delete
    # to release the needed memory to update.
    found = False
    while not found:
        res = min(result, key=lambda x: abs(x - need_to_free))
        if res < need_to_free:
            result.remove(res)
        else:
            found = True

    print(res)

    # Remove folder structure when done.
    shutil.rmtree('./out')


def get_folder_size(dir_path: str) -> int:
    """Recursively get the size of a directory."""
    count = 0
    with os.scandir(dir_path) as it:
        for entry in it:
            if entry.is_file():
                count += int(entry.name.split(".")[0])
            elif entry.is_dir():
                count += get_folder_size(f"{dir_path}/{entry.name}")
    return count

if __name__ == '__main__':
    main()
