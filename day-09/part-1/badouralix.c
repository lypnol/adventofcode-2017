#include <stdio.h>
#include <stdbool.h>

const int run(char* s)
{
    int current_value = 0,
        result = 0;
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
                break;
            }
        } else {
            switch (*c) {
            case '{':
                current_value++;
                break;
            case '}':
                result += current_value--;
                break;
            case '<':
                garbage = true;
                break;
            default:
                break;
            }
        }
    }

    return result;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
