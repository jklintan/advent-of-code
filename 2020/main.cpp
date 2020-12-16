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

list<int> testDay1{1721, 979, 366, 299, 675, 1456};

int main(int argc, char* argv[]) {
    
    // Day 1
#if 0
    list<int> inputDay1 = processInputNumbers("../../AdventOfCode/advent-of-code/2020/day1/input.txt");
    if (inputDay1.size() != 0) {
        cout << productOfSum2(inputDay1, 2020) << endl;
        cout << productOfSum3(inputDay1, 2020) << endl;
    }
#endif

    // Day 2
#if 0
    list<PasswordInput> passwordInput = processInputPasswords("../../AdventOfCode/advent-of-code/2020/day2/input.txt");
    cout << numbApprovedPasswords(passwordInput, "occurring") << endl;
    cout << numbApprovedPasswords(passwordInput, "specificPlace") << endl;
#endif

    return 1;
};