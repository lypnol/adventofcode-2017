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
    int64_t last_played = 0;
    int offset = 0;

    while (getline(input, line, '\n')) {
        lines.push_back(line);
    }

    while (offset >= 0 && offset < lines.size()) {
        line = lines[offset];
        istringstream tokens(line);
        tokens >> inst;
        tokens >> x;
        if (inst == "snd") {
            last_played = eval(reg, x);
        } else if (inst == "set") {
            tokens >> y;
            reg[x.at(0) - 'a'] = eval(reg, y);
        } else if (inst == "add") {
            tokens >> y;
            reg[x.at(0) - 'a'] += eval(reg, y);
        } else if (inst == "mul") {
            tokens >> y;
            reg[x.at(0) - 'a'] *= eval(reg, y);
        } else if (inst == "mod") {
            tokens >> y;
            reg[x.at(0) - 'a'] %= eval(reg, y);
        } else if (inst == "rcv") {
            if (eval(reg, x)) {
                return to_string(last_played);
            }
        } else if (inst == "jgz") {
            tokens >> y;
            if (eval(reg, x)) {
                offset += eval(reg, y);
                continue;
            }
        }
        offset++;
    }
    return "";
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}