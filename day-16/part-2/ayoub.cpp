#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <streambuf>
#include <unordered_map>

#define N 16
#define ROUNDS 1000000000

using namespace std;

typedef struct {
    char type; 
    size_t arg1;
    size_t arg2;
} instruction_t;

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

uint64_t dance(instruction_t *instructions, size_t n, uint64_t rounds = ROUNDS) {
    uint64_t index = 0x0123456789abcdefULL;
    uint64_t round = 0;
    bool loop_found = false;
    unordered_map<uint64_t, size_t> seen;

    while(round < rounds) {
        for (size_t i = 0; i < n; i++) {
            if (!loop_found && seen.find(index) != seen.end()) {
                if (seen.at(index) == i){
                    round *= (rounds / round);
                    loop_found = true;
                }
            }
            if (!loop_found) {
                seen.insert(make_pair(index, i));
            }

            switch(instructions[i].type) {
            case 's':
                index = spin(index, instructions[i].arg1);
                break;
            case 'x':
                index = exchange(index, instructions[i].arg1, instructions[i].arg2);
                break;
            case 'p':
                index = partner(index, instructions[i].arg1, instructions[i].arg2);
                break;
            }
        }
        
        round++;
    }
    return index;
}

string run(string s) {
    string instruction;
    istringstream input(s);
    int sep, a, b;
    size_t n = count(s.begin(), s.end(), ',')+1;
    instruction_t *instructions = (instruction_t*) malloc(n*sizeof(instruction_t));

    int i = 0;
    while (getline(input, instruction, ',')) {
        switch (instruction.at(0)) {
        case 's':
            instructions[i].type = 's';
            instructions[i].arg1 = stoi(instruction.substr(1));
            break;
        case 'x':
            sep = instruction.find('/');
            a = stoi(instruction.substr(1, sep-1));
            b = stoi(instruction.substr(sep+1));
            
            instructions[i].type = 'x';
            instructions[i].arg1 = a;
            instructions[i].arg2 = b;
            break;
        case 'p':
            a = (int)(instruction.at(1)-'a');
            b = (int)(instruction.at(3)-'a');

            instructions[i].type = 'p';
            instructions[i].arg1 = a;
            instructions[i].arg2 = b;
            break;
        }
        i++;
    }
    uint64_t index = dance(instructions, n);

    free(instructions);
    return index_to_string(index);
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}