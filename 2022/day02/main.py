"""Solution to advent of code day 2 2022."""

from enum import Enum


def main():
    """Main function for running day 2."""

    file_path = "input.txt"

    # Part 1
    game = ElfRockPaperScissorGame()
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            current_match = line.strip().split(" ")
            opponent_move = current_match[0].lower()
            my_move = current_match[1].lower()
            game.play(my_move, opponent_move)

        print(game.total_score)

    # Part 2
    reversed_tactics_game = ElfRockPaperScissorGame()
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            current_match = line.strip().split(" ")
            opponent_move = current_match[0].lower()
            my_desired_outcome = current_match[1].lower()

            move = reversed_tactics_game.decide_move(my_desired_outcome, opponent_move)
            reversed_tactics_game.play(move, opponent_move)

        print(reversed_tactics_game.total_score)


class PlayOutcome(Enum):
    """The different play outcomes possible."""

    WIN = 1
    TIE = 2
    LOSS = 3


class ElfRockPaperScissorGame:
    """Holds information about the whole game."""

    def __init__(self):
        """Initializes an unstarted game."""

        # Possible strings that represent a move
        # and what they are decoded to.
        self.moves = {
            "x": "rock",
            "y": "paper",
            "z": "scissors",
            "a": "rock",
            "b": "paper",
            "c": "scissors",
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors",
        }

        # Pair moves with their winning move.
        self.pair_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

        # Pairs strings with outcome representation.
        self.outcome_decoder = {
            "x": PlayOutcome.LOSS,
            "y": PlayOutcome.TIE,
            "z": PlayOutcome.WIN,
        }

        # Pairs a play with a score.
        self.play_score_decoder = {"rock": 1, "paper": 2, "scissors": 3}

        # Pairs a game outcome with a score.
        self.outcome_score_decoder = {
            PlayOutcome.LOSS: 0,
            PlayOutcome.TIE: 3,
            PlayOutcome.WIN: 6,
        }

        # Holds the total score for all games.
        self.total_score = 0

    def decide_move(self, needed_outcome: str, opponent_move: str) -> str:
        """Decides move to play given the opponent move and needed outcome"""
        move = self.outcome_decoder[needed_outcome]
        if move == PlayOutcome.WIN:
            return self.pair_moves[self.moves[opponent_move]]
        if move == PlayOutcome.LOSS:
            return [k for k, v in self.pair_moves.items() if v == self.moves[opponent_move]][0]
        return opponent_move

    def get_total_score(self):
        """Returns the current total score of the game."""
        return self.total_score

    def play(self, my_move: str, opponent_move: str) -> int:
        """Plays a single game vs one elf given my move and the elf's move."""
        if self.moves[my_move] == self.moves[opponent_move]:
            outcome = PlayOutcome.TIE
        elif (
            (self.moves[my_move] == "rock" and self.moves[opponent_move] == "scissors")
            or (self.moves[my_move] == "paper" and self.moves[opponent_move] == "rock")
            or (self.moves[my_move] == "scissors" and self.moves[opponent_move] == "paper")
        ):
            outcome = PlayOutcome.WIN
        else:
            outcome = PlayOutcome.LOSS

        this_play_score = (
            self.play_score_decoder[self.moves[my_move]] + self.outcome_score_decoder[outcome]
        )
        self.total_score += this_play_score
        return this_play_score


if __name__ == "__main__":
    main()
