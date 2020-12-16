#ifndef DAY1
#define DAY1

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

// Calculate the product of the sum of two terms that adds up to input specific number, if existing in input
int productOfSum2(list<int> l, int sum) {

    int goal{ sum };
    int missing{ 0 };
    int currentItem{ 0 };

    l.sort();

    for (list<int>::iterator it = l.begin(); it != l.end(); ++it) {
        currentItem = *it;

        if (currentItem > goal)
            return 0;

        missing = goal - currentItem;

        auto it2 = find(next(it), l.end(), missing);
        if (it2 != l.end()) {
            return (*it2) * currentItem;
        }
    }

    return 0; // No pairs found
};

// Calculate the product of the sum of three terms that adds up to input specific number, if existing in input
int productOfSum3(list<int> l, int sum) {

    int goal{ sum };
    int missing{ 0 };
    int currentItem{ 0 };
    int nextItem{ 0 };

    l.sort();

    for (list<int>::iterator it = l.begin(); it != l.end(); ++it) {

        currentItem = *it;
        if (currentItem > goal)
            return 0;

        missing = goal - currentItem;

        if (missing > 0) {
            for (list<int>::iterator it2 = next(it); it2 != l.end(); ++it2) {
                nextItem = *it2;
                missing = goal - nextItem - currentItem;

                if (missing < 0)
                    break;

                auto missingTerm = find(next(it2), l.end(), missing);
                if (missingTerm != l.end())
                    return (*missingTerm) * nextItem * currentItem;
            }
        }
    }

    return 0; // No triple found
};

#endif 