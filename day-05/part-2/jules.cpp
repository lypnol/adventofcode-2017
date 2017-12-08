#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
using namespace std;

string run(string s) {
    string   line;
    vector<int>    instructions;
    stringstream ss(s);

    while(getline(ss, line, '\n'))
    {
        int value;
        value = atoi(line.c_str());
        instructions.push_back(value);
    }
    int offset = 0;
    int old_offset = 0;
    int length = instructions.size();
    int counter = 0;
    while(offset >= 0 && offset < length) {
        counter++;
        old_offset = offset;
        offset += instructions[offset];
        if(instructions[old_offset] >= 3){
            instructions[old_offset]--;
        }
        else
        {
            instructions[old_offset]++;
        }
    }
    return to_string(counter);
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}