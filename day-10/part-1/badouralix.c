#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define circle_size 256
#define a *(circle + (current_position + i) % circle_size)
#define b *(circle + (current_position + length - 1 - i) % circle_size)

const int run(char* s)
{
    int circle[circle_size], buffer[circle_size],
        current_position = 0, skip_size = 0, length;

    const char delimiters[] = ",";
    char *token = strtok(s, delimiters);

    for (int i = 0; i != circle_size; i++) {
        circle[i] = i;
    }

    do {
        length = atoi(token);
        for (int i = 0; 2*i + 1 < length; i++) {
            a ^= b ^= a ^= b;
        }
        current_position = (current_position + length + skip_size) % circle_size;
        skip_size++;
    } while (token = strtok(NULL, delimiters));

    return circle[0] * circle[1];
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
