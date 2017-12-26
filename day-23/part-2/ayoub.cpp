#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>

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

int is_prime(int64_t n) {
    for (int64_t i = 2; i <= n / 2; ++i) {
        if (n % i == 0) return 0;
    }
    return 1;
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

    reg[0] = 1;

    while (getline(input, line, '\n')) {
        lines.push_back(line);
    }

    for (size_t i = 0; i < lines.size() - 15; i++) {
        if (lines[i   ].substr(0, 3) == "set" && lines[i].substr(6, 1) == "1" &&
            lines[i+1 ].substr(0, 3) == "set" && lines[i+1].substr(6, 1) == "2" &&
            lines[i+2 ].substr(0, 3) == "set" && lines[i+2].substr(6, 1) == "2" &&
            lines[i+3 ].substr(0, 3) == "set" && lines[i+3].substr(6, 1) == lines[i+1].substr(4, 1) &&
            lines[i+4 ].substr(0, 3) == "mul" && lines[i+4].substr(4, 1) == lines[i+3].substr(4, 1) && lines[i+4].substr(6, 1) == lines[i+2].substr(4, 1) &&
            lines[i+5 ].substr(0, 3) == "sub" && lines[i+5].substr(4, 1) == lines[i+4].substr(4, 1) &&
            lines[i+6 ].substr(0, 3) == "jnz" && lines[i+6].substr(4, 1) == lines[i+5].substr(4, 1) && lines[i+6].substr(6, 1) == "2" &&
            lines[i+7 ].substr(0, 3) == "set" && lines[i+7].substr(4, 1) == lines[i].substr(4, 1) && lines[i+7].substr(6, 1) == "0" &&
            lines[i+8 ].substr(0, 3) == "sub" && lines[i+8].substr(4, 1) == lines[i+2].substr(4, 1) && lines[i+8].substr(6, 2) == "-1" &&
            lines[i+9 ].substr(0, 3) == "set" && lines[i+9].substr(4, 1) == lines[i+6].substr(4, 1) && lines[i+9].substr(6, 1) == lines[i+2].substr(4, 1) &&
            lines[i+10].substr(0, 3) == "sub" && lines[i+10].substr(4, 1) == lines[i+9].substr(4, 1) &&
            lines[i+11].substr(0, 3) == "jnz" && lines[i+11].substr(4, 1) == lines[i+10].substr(4, 1) && lines[i+11].substr(6, 2) == "-8" &&
            lines[i+12].substr(0, 3) == "sub" && lines[i+12].substr(4, 1) == lines[i+1].substr(4, 1) && lines[i+12].substr(6, 2) == "-1" &&
            lines[i+13].substr(0, 3) == "set" && lines[i+13].substr(4, 1) == lines[i+11].substr(4, 1) && lines[i+13].substr(6, 1) == lines[i+1].substr(4, 1) &&
            lines[i+14].substr(0, 3) == "sub" && lines[i+14].substr(4, 1) == lines[i+13].substr(4, 1) && lines[i+14].substr(6, 1) == lines[i+5].substr(6, 1) &&
            lines[i+15].substr(0, 3) == "jnz" && lines[i+15].substr(4, 1) == lines[i+14].substr(4, 1) && lines[i+15].substr(6, 3) == "-13") {
            char b, d, e, f, g;
            b = lines[i+10].at(6);
            f = lines[i].at(4);
            d = lines[i+1].at(4);
            e = lines[i+2].at(4);
            g = lines[i+3].at(4);
            lines[i] = "prm " + string(&f, 1) + " " + string(&b, 1) + " " + string(&d, 1) + " " + string(&e, 1) + " " + string(&g, 1);
            for (size_t j = i+1; j < i+16; j++) {
                lines[j] = "";
            }
            break;
        }
    }

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
            tokens >> y;
            reg[x.at(0) - 'a'] *= eval(reg, y);
        } else if (inst == "jnz") {
            tokens >> y;
            if (eval(reg, x) != 0) {
                offset += eval(reg, y);
                continue;
            }
        } else if (inst == "prm") {
            string f, b, g, d, e;
            f = x;
            tokens >> b;
            tokens >> d;
            tokens >> e;
            tokens >> g;
            reg[f.at(0)-'a'] = is_prime(reg[b.at(0)-'a']);
            reg[d.at(0)-'a'] = reg[b.at(0)-'a'];
            reg[e.at(0)-'a'] = reg[b.at(0)-'a'];
            reg[g.at(0)-'a'] = 0;
            offset += 16;
            continue;
        }
        offset++;
    }
    return to_string(reg['h'-'a']);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cout << "Missing one argument" << endl;
        exit(1);
    }
    cout << run(string(argv[1])) << "\n";
    return 0;
}