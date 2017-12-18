#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int run(string s) {
    int move;
    int pos = 0;
    int return_value = 0;
    move = atoi(s.c_str());
    vector<int> circular;
    for(int i = 1; i < 50000001; i++){
        pos = (pos + move) % i;
        return_value = (pos == 0) ? i : return_value;
        pos++;
    }
    return return_value;
}

int main(int argc, char** argv) {
    if(argc < 2){
        cout << "Missing one argument" << endl;
        exit(1);
    }
    cout << run(string(argv[1])) << "\n";
    return 0;
}