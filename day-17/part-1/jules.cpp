#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int run(string s) {
	int move;
    int pos = 0;
    move = atoi(s.c_str());
    vector<int> circular;
    for(int i = 1; i < 2018; i++){
        pos = (pos + move) % i;
        if(pos == circular.size()){
            circular.push_back(i);
        }
        else
        {
            vector<int>::iterator it = circular.begin() + (pos + 1);
            circular.insert(it, i);
        }
        pos++;
    }
    vector<int>::iterator position = find(circular.begin(), circular.end(), 2017);
    return *(position + 1);
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}