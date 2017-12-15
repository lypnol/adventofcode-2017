#include <iostream>
#include <string>
#include <sstream>

#define GEN_A   0x00000000000041A7
#define GEN_B   0x000000000000BC8F
#define MOD     0x000000007FFFFFFF
#define ROUNDS  0x0000000002625A00

using namespace std;

bool is_match(uint64_t A, uint64_t B) {
    A &= 0x000000000000FFFF;
    B &= 0x000000000000FFFF;
    return A == B;
}

int count_matches(uint64_t N, uint64_t A, uint64_t B) {
    int count = 0;
    while (N--) {
        A = (A*GEN_A)%MOD;
        B = (B*GEN_B)%MOD;
        if (is_match(A, B)) count++;
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