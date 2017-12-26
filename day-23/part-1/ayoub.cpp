#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>


using namespace std;

bool is_number(const string& s) {
    for (size_t i = 0; i < s.size(); i++) {
        if ((s.at(i) >= '0' && s.at(i) <= '9') || (i == 0 && s.at(i) == '-')) {
            continue;
        }
        return false;
    }
    return true;
}

int64_t eval(int64_t *reg, string& value) {
    if (is_number(value)) {
        return stoll(value);
    } else if (value.size() == 1) {
        return reg[value.at(0) - 'a'];
    }
    cerr << "Couldn't evaluate expression " << value << "\n";
    return 0;
}

string run(string s) {
	istringstream input(s);
    vector<string> lines;
    string line;
    string inst, x, y;
    int64_t reg[26] = {0};
    int offset = 0;

    while (getline(input, line, '\n')) {
        lines.push_back(line);
    }

    uint64_t multcount = 0;

    while (offset >= 0 && offset < lines.size()) {
        line = lines[offset];
        istringstream tokens(line);
        tokens >> inst;
        tokens >> x;
        if (inst == "set") {
            tokens >> y;
            reg[x.at(0) - 'a'] = eval(reg, y);
        } else if (inst == "sub") {
            tokens >> y;
            reg[x.at(0) - 'a'] -= eval(reg, y);
        } else if (inst == "mul") {
            multcount++;
            tokens >> y;
            reg[x.at(0) - 'a'] *= eval(reg, y);
        } else if (inst == "jnz") {
            tokens >> y;
            if (eval(reg, x) != 0) {
                offset += eval(reg, y);
                continue;
            }
        }
        offset++;
    }
    return to_string(multcount);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cout << "Missing one argument" << endl;
        exit(1);
    }
    cout << run(string(argv[1])) << "\n";
    return 0;
}