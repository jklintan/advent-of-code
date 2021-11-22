#ifndef DAY3
#define DAY3

#include <vector>

using namespace std;

int traverseMap(int sideways, int down, vector<string> map) {
    // We assume a positive value of sideways is right
    // and negative is to the left and that we always
    // go downwards.

    int treesEncountered = 0;
    int rows = map.size();
    int currentRow = 0;
    int currentCol = 0;
    int columns = map[0].length();

    // We assume that all map rows are of equal length.
    while (currentRow <= rows) {
        char curr = map[currentRow][currentCol];
        if (curr == '#') {
            treesEncountered += 1;
        }
        currentRow += down;
        currentCol += sideways;
        if (currentCol > columns - 1) {
            currentCol -= columns;
        }
        if (currentRow >= rows) {
            break;
        }
    }
    return treesEncountered;
}

vector<string> readMap(string fileName) {
    // ifstream inputFile;
    // inputFile.open(fileName, ios::in);
    vector<string> lines;
    ifstream input(fileName);
    string line;
    while (getline(input, line))
    {
        lines.push_back(line);
    }
    return lines;
}

#endif