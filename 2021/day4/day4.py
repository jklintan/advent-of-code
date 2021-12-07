"""Solutions to day 4 of advent of code 2021."""

from typing import List, Optional
import numpy as np

def main() -> None:
    """Main function for day 4 solutions."""

    # Read in bingo tiles and store in bingo game.
    lines = open("./input.txt").read().splitlines()
    lines = [i for i in lines if i]

    bingo_game = BingoGame()
    bingo_numbers = lines[0].split(',')
    bingo_game.add_bingo_numbers([int(bingo_number) for bingo_number in bingo_numbers])

    i = 1
    while i <= len(lines) - 5:

        bingo_str = ""
        for k in range(5):
            bingo_str += lines[i + k] + " "
        i += 5

        bingo_tile = [int(bingo_number) for bingo_number in bingo_str.split(" ") if bingo_number]
        bingo_game.add_tile(BingoTile(np.array(bingo_tile).reshape(5, 5)))

    if bingo_game.play_bingo():
        print(bingo_game.calculate_winning_score())  # Part 1

    if(bingo_game.play_bingo_squid()):
        print(bingo_game.calculate_losing_score())  # Part 2
    

class BingoTile():
    """Class representing a bingo-tile."""

    def __init__(self, numbers: np.array) -> None:
        """Initializes a bingo-tile of shp (5,5)."""
        self.numbers = numbers
        self.bingo = False
        self.marked = np.zeros((5, 5))

    def check_bingo(self) -> bool:
        """Checks if bingo-tile has gotten bingo."""
        for row in range(5):
            if np.sum(self.marked[row, :]) == 5:
                self.bingo = True
                return True

        for col in range(self.marked.shape[1]):
            if np.sum(self.marked[:, col]) == 5:
                self.bingo = True
                return True

        return False

    def check_number(self, number: int) -> None:
        """Checks for number on bingo-tile."""
        index = np.where(self.numbers == number)
        if len(index) != 0:
            self.marked[index[0], index[1]] = 1

    def calculate_score(self, bingo_num: int) -> int:
        """Calculates the score for the tile."""
        marked = self.marked.flatten()
        score = 0
        for i, num in enumerate(self.numbers.flatten()):
            if marked[i] == 0:
                score += num

        return score * bingo_num



class BingoGame():
    """Class representing a game of bingo on the submarine."""

    def __init__(self) -> None:
        """Initializes a bingo game."""
        self.bingo_tiles = []
        self.numbers = []
        self.winning_tile = None
        self.winning_num = None
        self.losing_tile = None
        self.last_num = None

    def add_bingo_numbers(self, numbers: List[int]) -> None:
        """Add bingo numbers for the game."""
        self.numbers = numbers

    def add_tile(self, bingo_tile: BingoTile) -> None:
        """Adds a bingo-tile to the game."""
        self.bingo_tiles.append(bingo_tile)

    def check_bingo(self) -> Optional[BingoTile]:
        """Checks for bingo among the bingo-tiles for the current game."""
        for bingo_tile in self.bingo_tiles:
            if bingo_tile.check_bingo():
                return bingo_tile
        return None

    def check_bingo_squid(self) -> None:
        """Checks for bingo vs the squid, rmvs tiles that have gotten bingo"""
        for bingo_tile in self.bingo_tiles:
            if bingo_tile.check_bingo():
                self.bingo_tiles.remove(bingo_tile)

    def play_bingo(self) -> bool:
        """Plays bingo by finding the first winning tile."""
        for num in self.numbers:
            for bingo_tile in self.bingo_tiles:
                bingo_tile.check_number(num)

            winner = self.check_bingo()
            if winner:
                self.winning_tile = winner
                self.winning_num = num
                return True

        return False

    def play_bingo_squid(self) -> bool:
        """Plays bingo vs the squid and lets it win.
        
        We let the squid win by finding the last tile that
        should have gotten bingo given the bingo-numbers.
        """
        for num in self.numbers:
            for bingo_tile in self.bingo_tiles:
                bingo_tile.check_number(num)

            self.check_bingo_squid()
            if len(self.bingo_tiles) == 1:
                self.losing_tile = self.bingo_tiles[0]
                self.last_num = num
                return True

        return False

    def calculate_winning_score(self) -> int:
        """Calculate the winning tile's score."""
        if self.winning_tile:
            return self.winning_tile.calculate_score(self.winning_num)

    def calculate_losing_score(self) -> int:
        """Calculate the losing tile's score."""
        if self.losing_tile:
            return self.losing_tile.calculate_score(self.last_num)


if __name__ == '__main__':
    main()