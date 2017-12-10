#include <stdio.h>
#include <stdbool.h>

const int run(char* s)
{
    int counter = 0;
    bool garbage = false;

    for (char* c = --s; *++c != '\0';) {
        if (garbage) {
            switch (*c) {
            case '!':
                c++;
                break;
            case '>':
                garbage = false;
                break;
            default:
                counter++;
                break;
            }
        } else {
            switch (*c) {
            case '<':
                garbage = true;
                break;
            default:
                break;
            }
        }
    }

    return counter;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
