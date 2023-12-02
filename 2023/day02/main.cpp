// Advent of code day 2 2023.

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <math.h>


void updateGameData(std::vector<size_t>& gameData, std::vector<size_t>& maximumValues, size_t& entry, const size_t idx) {
    gameData[idx] = entry;
    if (entry > maximumValues[idx]) {
        maximumValues[idx] = entry;
    }
    entry = 0;
}

int main()
{
    std::ifstream inputFile;
    inputFile.open("./input.txt", std::ios::in);

    const std::vector<size_t> availableCubes = { 12, 13, 14 };

    std::vector<size_t> maximumValues(3, 0);
    std::vector<size_t> currentGame(3, 0);

    size_t part1 = 0;
    size_t part2 = 0;

    if (inputFile.is_open()) {
        std::string word;
        size_t entry = 0;
        size_t gameId = 0;
        bool evaluateGame = false;
        bool allGamesSucceeded = true;
        while (inputFile >> word)
        {
            // Remove any trailing comma.
            word.erase(remove(word.begin(), word.end(), ','), word.end());

            // End of a subgame, evaluate sub-game at the end of this iteration.
            if (word.back() == ';') {
                word.erase(remove(word.begin(), word.end(), ';'), word.end());
                evaluateGame = true;
            }

            // If we have a ':', we know the current game is about to begin.
            if (word.back() == ':') {
                word.erase(remove(word.begin(), word.end(), ':'), word.end());
                gameId = std::stoi(word);
            }
            else if (word == "Game") {
                const bool gamePossible = std::equal(std::begin(currentGame), std::end(currentGame),
                    std::begin(availableCubes), std::end(availableCubes),
                    [](size_t a, size_t b)->bool {return a <= b; });

                // If the last game succeeded and all previous ones for
                // this game ID succeeded (and we are not in the very first
                // case at the start of processing), we add to the sum
                // of possible games.
                if (gamePossible && allGamesSucceeded && gameId != 0) {
                    part1 += gameId;
                }
                evaluateGame = false;
                currentGame = { 0, 0, 0 };
                allGamesSucceeded = true;

                // Each time we start a new game and evaluate the last
                // we add the power of the minimum set of cubes possible.
                part2 += (maximumValues[0] * maximumValues[1] * maximumValues[2]);
                maximumValues = { 0, 0, 0 };
            }
            else if (word == "red") {
                updateGameData(currentGame, maximumValues, entry, 0);
            }
            else if (word == "green") {
                updateGameData(currentGame, maximumValues, entry, 1);
            }
            else if (word == "blue") {
                updateGameData(currentGame, maximumValues, entry, 2);
            }
            else {
                // We only end up in this case if we have a
                // number as an entry. We save this one for
                // this evaluation and it will be stored
                // depending on the next word in the input.
                entry = std::stoi(word);
            }

            // If we should evaluate a sub game, we do
            // so and check if all games for this ID
            // has kept on succeeding or not.
            if (evaluateGame) {
                const bool gameSucceeded = std::equal(std::begin(currentGame), std::end(currentGame),
                    std::begin(availableCubes), std::end(availableCubes),
                    [](size_t a, size_t b)->bool {return a <= b; });
                if (!gameSucceeded) {
                    allGamesSucceeded = false;
                }

                evaluateGame = false;
            }
        }

        // Check the final one.
        const bool currentGameSucceeded = std::equal(std::begin(currentGame), std::end(currentGame),
            std::begin(availableCubes), std::end(availableCubes),
            [](size_t a, size_t b)->bool {return a <= b; });

        if (currentGameSucceeded && allGamesSucceeded) {
            part1 += gameId;
        }
        part2 += (maximumValues[0] * maximumValues[1] * maximumValues[2]);

        inputFile.close(); //close the file object.


    }

    std::cout << part1 << std::endl;
    std::cout << part2 << std::endl;
}
