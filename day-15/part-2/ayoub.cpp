#include <iostream>
#include <string>
#include <sstream>

#define GEN_A   0x00000000000041A7
#define GEN_B   0x000000000000BC8F
#define MOD     0x000000007FFFFFFF
#define ROUNDS  0x00000000004C4B40

using namespace std;

bool is_match(uint64_t A, uint64_t B) {
    A &= 0x000000000000FFFF;
    B &= 0x000000000000FFFF;
    return A == B;
}

int count_matches(uint64_t N, uint64_t A, uint64_t B) {
    int count = 0;
    bool foundA = false, foundB = false;
    while (N) {
        if (!foundA) {
            A = (A*GEN_A)%MOD;
            foundA = A%0x0000000000000004 == 0;
        }
        if (!foundB) {
            B = (B*GEN_B)%MOD;
            foundB = B%0x0000000000000008 == 0;
        }
        if (foundA && foundB) {
            if (is_match(A, B)) count++;
            N--;
            foundA = false;
            foundB = false;
        }
    }

    return count;
}

string run(string s) {
    istringstream input(s);
    string null;
    uint64_t A, B;
    for (int i = 0; i < 4; i++) input >> null;
    input >> A;
    for (int i = 0; i < 4; i++) input >> null;
    input >> B;
    return to_string(count_matches(ROUNDS, A, B));
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}