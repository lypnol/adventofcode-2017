#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <string>

using namespace std;


typedef struct {
    int64_t x, y, z;
} coord_t;

typedef struct {
    coord_t p, v, a;
    bool removed;
} kinetic_t;

void get_numbers(string line, vector<string>& match) {
    string number = "";
    for (size_t i = 0; i < line.size(); i++) {
        if (line.at(i) == '-' || (line.at(i) >= '0' && line.at(i) <= '9')) {
            number.append(1, line.at(i));
        } else if (number.size()) {
            match.push_back(number);
            number.clear();
        }
    }
}

kinetic_t parse_line(string line) {
    kinetic_t res;
    vector<string> match;
    get_numbers(line, match);

    res.p.x = stoi(match[0]);
    res.p.y = stoi(match[1]);
    res.p.z = stoi(match[2]);

    res.v.x = stoi(match[3]);
    res.v.y = stoi(match[4]);
    res.v.z = stoi(match[5]);

    res.a.x = stoi(match[6]);
    res.a.y = stoi(match[7]);
    res.a.z = stoi(match[8]);

    res.removed = false;

    return res;
}

bool simulate(vector<kinetic_t>& particles) {
    for (size_t i = 0; i < particles.size(); i++) {
        if (particles[i].removed) continue;

        particles[i].v.x += particles[i].a.x;
        particles[i].v.y += particles[i].a.y;
        particles[i].v.z += particles[i].a.z;

        particles[i].p.x += particles[i].v.x;
        particles[i].p.y += particles[i].v.y;
        particles[i].p.z += particles[i].v.z;
    }

    bool collision = false;
    for (size_t i = 0; i < particles.size(); i++) {
        if (particles[i].removed) continue;
        for (size_t j = i+1; j < particles.size(); j++) {
            if (particles[j].removed) continue;
            if (particles[i].p.x == particles[j].p.x && 
                particles[i].p.y == particles[j].p.y &&
                particles[i].p.z == particles[j].p.z) {
                
                particles[i].removed = true;
                particles[j].removed = true;
                collision = true;
            }
        }
    }
    return collision;
}

size_t cout_left(vector<kinetic_t>& particles) {
    size_t res = 0;
    for (size_t i = 0; i < particles.size(); i++) {
        if (!particles[i].removed) res++;
    }
    return res;
}

string run(string s) {
	istringstream input(s);
    string line;
    vector<kinetic_t> particles;

    while (getline(input, line, '\n')) {
        if(line.size() == 0) continue;
        particles.push_back(parse_line(line));
    }

    bool collision = false;
    int64_t frames = 1000;
    do {
        collision = simulate(particles);
        if (collision) frames = 1000;
        else frames--;
    } while(frames);

    return to_string(cout_left(particles));
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cout << "Missing one argument" << endl;
        exit(1);
    }
    cout << run(string(argv[1])) << "\n";
    
    return 0;
}