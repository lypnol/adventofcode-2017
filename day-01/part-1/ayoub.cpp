#include <iostream>
#include <string>
#include <vector>

using namespace std;

string run(string s) {
	int sum = 0;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == s[(i + 1) % s.size()]) {
            sum += s[i] - '0';
        }
    }
    return to_string(sum);
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}