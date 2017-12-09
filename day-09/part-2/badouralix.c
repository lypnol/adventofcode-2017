#include <stdio.h>
#include <stdbool.h>

const int run(char* s)
{
    int counter = 0;
    bool garbage = false;

    for (char* c = --s; *++c != '\0';) {
        switch (*c) {
        case '!':
            c++;
            break;
        case '<':
            if (garbage) counter++;
            else garbage = true;
            break;
        case '>':
            garbage = false;
            break;
        default:
            if (garbage) counter++;
            break;
        }
    }

    return counter;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
