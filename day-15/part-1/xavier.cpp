#include <iostream>
#include <string>
#include <sstream>
#include <random>

using namespace std;

string run(string s) {
    string line;
    stringstream ss(s);
    getline(ss, line, '\n');
    int seedA = stoi(line.c_str() + 24);
    getline(ss, line, '\n');
    int seedB = stoi(line.c_str() + 24);

    minstd_rand0 genA;
    minstd_rand genB;

    genA.seed(seedA);
    genB.seed(seedB);

    int counter = 0;

    for(int i = 0; i<40000000; i++){

        if ((genA() & 0xffff) == (genB() & 0xffff)){
            counter++;
        }
    }
    return to_string(counter);
}


int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}