#include <stdio.h>
#include <stdbool.h>

const int run(char* s)
{
    int current_value = 0,
        result = 0;
    bool garbage = false;

    for (char* c = --s; *++c != '\0';) {
        switch (*c) {
        case '!':
            c++;
            break;
        case '{':
            if (!garbage) current_value++;
            break;
        case '}':
            if (!garbage) result += current_value--;
            break;
        case '<':
            garbage = true;
            break;
        case '>':
            garbage = false;
            break;
        default:
            break;
        }
    }

    return result;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
