#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>


using namespace std;

uint64_t spin(uint64_t index, size_t x) {
    return (index << (64-4*x)) | (index >> (4*x));
}

uint64_t exchange(uint64_t index, size_t a, size_t b) {
    size_t i = 64-4*(a+1), j = 64-4*(b+1);
    uint64_t x = ((index >> i) ^ (index >> j)) & ((1U << 4) - 1);
    return index ^ ((x << i) | (x << j));
}

uint64_t partner(uint64_t index, size_t x, size_t y) {
    size_t a, b;
    for (size_t i = 0; i < 16; i++) {
        uint64_t mask = 0xf000000000000000ULL >> (i*4);
        size_t value = (size_t)((mask & index) >> (64-(i+1)*4));
        if (value == x) a = i;
        if (value == y) b = i;
    }
    return exchange(index, a, b);
}

string index_to_string(uint64_t index) {
    char output[17];
    for (size_t i = 0; i < 16; i++) {
        uint64_t mask = 0xf000000000000000ULL >> (i*4);
        output[i] = (char)((index & mask) >> (64-(i+1)*4)) + 'a';
    }
    output[16] = '\0';
    return string(output);
}

string run(string s) {
	uint64_t index = 0x0123456789abcdefULL;
    string instruction;
    istringstream input(s);
    size_t sep, a, b;

    while (getline(input, instruction, ',')) {
        switch (instruction.at(0)) {
        case 's':
            index = spin(index, (size_t)stoi(instruction.substr(1)));
            break;
        case 'x':
            sep = instruction.find('/');
            a = (size_t)stoi(instruction.substr(1, sep-1));
            b = (size_t)stoi(instruction.substr(sep+1));
            index = exchange(index, a, b);
            break;
        case 'p':
            a = (size_t)(instruction.at(1)-'a');
            b = (size_t)(instruction.at(3)-'a');
            index = partner(index, a, b);
            break;
        }
    }

    return index_to_string(index);
}

int main(int argc, char** argv) {
    if(argc < 2){
        cout << "Missing one argument" << endl;
        exit(1);
    }
    cout << run(string(argv[1])) << "\n";
    return 0;
}