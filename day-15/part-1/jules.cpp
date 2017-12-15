#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
using namespace std;

int run(string s) {
    string   line;
    unsigned long a, b;
    stringstream ss(s);

    getline(ss, line, '\n');
    a = atoi(line.c_str() + 24);
    getline(ss, line, '\n');
    b = atoi(line.c_str() + 24);
    int genA =  16807, genB = 48271, n = 2147483647;
    int i = 0, score = 0;
    while(i < 40000000){
        i++;
        if((a & 0xffff) == (b & 0xffff)) {
            score++;
        }
        a = (a * genA) % n;
        b = (b * genB) % n;
    }
    return score;
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}