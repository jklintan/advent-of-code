#include <iostream>
#include <cstdlib>
#include <list>
#include <fstream>
#include <filesystem>
#include <stdio.h>
#include <string>

using namespace std;

#include "day1/day1.h"
#include "day2/day2.h"
#include "day3/day3.h"

list<int> testDay1{1721, 979, 366, 299, 675, 1456};

int main(int argc, char* argv[]) {
    
    // Day 1
#if 0
    list<int> inputDay1 = processInputNumbers("../../AdventOfCode/advent-of-code/2020/day1/input.txt");
    if (inputDay1.size() != 0) {
        cout << productOfSum2(inputDay1, 2020) << endl; // Part 1
        cout << productOfSum3(inputDay1, 2020) << endl; // Part 2
    }
#endif

    // Day 2
#if 0
    list<PasswordInput> passwordInput = processInputPasswords("../../AdventOfCode/advent-of-code/2020/day2/input.txt");
    cout << numbApprovedPasswords(passwordInput, "occurring") << endl; // Part 1
    cout << numbApprovedPasswords(passwordInput, "specificPlace") << endl; // Part 2
#endif

    // Day 3
#if 0
    vector<string> map = readMap("../../AdventOfCode/advent-of-code/2020/day3/input.txt");
    cout << "Trees encountered: " << traverseMap(3, 1, map) << endl; // Part 1
    cout << "Product = " << traverseMap(1, 1, map) * traverseMap(3, 1, map) * traverseMap(5, 1, map) * traverseMap(7, 1, map) * traverseMap(1, 2, map) << endl;
#endif

    return 1;
};