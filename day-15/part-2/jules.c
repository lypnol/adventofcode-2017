#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int run(char* s)
{
    unsigned long a, b;
    char *token = strtok(s, "\n");
    a = atoi(token+24);
    token = strtok(NULL, "\n");
    b = atoi(token+24);
    int genA =  16807, genB = 48271, n = 2147483647;
    int i = 0, score = 0;
    while(i < 5000000){
        i++;
        do {
            a = (a * genA) % n;
        } while ((a & 0x4) != 0);
        do {
            b = (b * genB) % n;
        } while ((b & 0x8) != 0);
        if((a & 0xffff) == (b & 0xffff)) {
            score++;
        }
    }
    return score;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
