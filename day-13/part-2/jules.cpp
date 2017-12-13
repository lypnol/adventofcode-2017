#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int run(string s) {
    string   line;
    map<int,int> firewall;
    stringstream ss(s);

    while(getline(ss, line, '\n'))
    {
        stringstream temp_ss(line);
        string layer, depth;
        getline(temp_ss, layer, ':');
        getline(temp_ss, depth, ':');
        firewall[atoi(layer.c_str())] = atoi(depth.c_str());
        
    }
    int delay = 0;
    while(true){
        bool spotted = false;
        for(auto elem : firewall)
        {
            if((elem.first + delay) % (elem.second * 2 - 2) == 0){
                spotted = true;
            }
        }
        if(spotted){
            delay++;
        }
        else{
            break;
        }
    }
    return delay;
}

int main(int argc, char** argv) {
    cout << run(string(argv[1])) << "\n";
    return 0;
}