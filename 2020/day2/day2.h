#ifndef DAY2
#define DAY2

#include <algorithm>

class PasswordInput {
public:
    PasswordInput() = default;
    PasswordInput(int mini, int maxi, char l, string p) { min = mini; max = maxi; let = l; password = p; };

    ~PasswordInput() = default;

    int min;
    int max;
    char let;
    string password;
};

list<PasswordInput> processInputPasswords(string name) {
    ifstream inputFile;
    inputFile.open(name, ios::in);

    list<PasswordInput> processed;

    if (inputFile.is_open()) {
        string w, line, word, password;
        int min{ 0 }, max{ 0 };
        char let;

        while (getline(inputFile, line)) {
            int count{ 0 }, len{ line.size() }, i{ 0 };

            for (auto x : line)
            {
                if (x == '-' && count == 0) {
                    min = stoi(word);
                    count++;
                    word = "";
                }
                else if (x == ':') {
                    let = *word.c_str();
                    count++;
                    word = "";
                }else if (x == ' ') {
                    if (count == 1) {
                        max = stoi(word);
                        count++;
                    }
                    word = "";
                }
                else {
                    word = word + x;
                    if (i == len-1) {
                        password = word;
                    }
                }
                ++i;
            }

            PasswordInput pI{ min, max, let, password};
            processed.push_back(pI);
            count = 0;
        }
        inputFile.close(); //close the file object.
    }

    return processed;
}

int numbApprovedPasswords(list<PasswordInput> pI, string rule) {
    int numbApproved{ 0 };

    if (rule == "occurring") {
        for (list<PasswordInput>::iterator it = pI.begin(); it != pI.end(); ++it) {
            size_t n = count((*it).password.begin(), (*it).password.end(), (*it).let);
            if (n <= (*it).max && n >= (*it).min)
                numbApproved++;
        }
    }
    else if (rule == "specificPlace") {
        for (list<PasswordInput>::iterator it = pI.begin(); it != pI.end(); ++it) {
            int pos1 = (*it).min - 1;
            int pos2 = (*it).max - 1;
            if ((*it).password.length() >= pos2) {
                if (((*it).let == (*it).password[pos1] && (*it).let != (*it).password[pos2]) || ((*it).let != (*it).password[pos1] && (*it).let == (*it).password[pos2]))
                    numbApproved++;
            }
            else {
                if ((*it).password.length() >= pos1) {
                    if ((*it).let == (*it).password[pos1]) {
                        numbApproved++;
                    }
                }
            }
        }
    }

    return numbApproved;
}

#endif