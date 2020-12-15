#include <iostream>
#include <cstdlib>
#include <list>
#include <fstream>
#include <filesystem>
#include <stdio.h>
#include <string>

using namespace std;

#include "day1/day1.h"

list<int> testDay1{1721, 979, 366, 299, 675, 1456};

list<int> processInputNumbers(string name) {
    ifstream inputFile;
    inputFile.open(name, ios::in);

    list<int> processed;
    int numb;

    if (inputFile.is_open()) {
        string w;
        while (getline(inputFile, w)) {
            processed.push_back(stoi(w));
        }
        inputFile.close(); //close the file object.
    }

    return processed;
}

int main(int argc, char* argv[]) {
    
    // Day 1
#if 0
    list<int> inputDay1 = processInputNumbers("../../AdventOfCode/advent-of-code/2020/day1/input.txt");
    if (inputDay1.size() != 0) {
        cout << productOfSum2(inputDay1, 2020);
        cout << productOfSum3(inputDay1, 2020);
    }
#endif

    return 1;
};