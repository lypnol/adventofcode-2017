#include <stdio.h>
#include <stdlib.h>

#define circle_size 256
#define m *(circle + (*current_position + i) % circle_size)
#define n *(circle + (*current_position + length - 1 - i) % circle_size)

void run_round(int* circle, const int* lengths, const int lengths_size, int* current_position, int* skip_size)
{
    int length;

    for (int i = 0; i != lengths_size; i++) {
        length = lengths[i];
        for (int i = 0; 2*i + 1 < length; i++) {
            (m ^= n), (n ^= m), (m ^= n);
        }
        *current_position = (*current_position + length + *skip_size) % circle_size;
        (*skip_size)++;
    }
}

const char* run(char* s)
{
    int circle[circle_size], lengths[circle_size],
        current_position = 0, skip_size = 0, lengths_size = 0, xor;

    char *output = malloc(sizeof(char) * 32);

    for (int i = 0; i != circle_size; i++) {
        circle[i] = i;
    }

    for (char* c = s; *c != '\0'; c++) {
        lengths[lengths_size++] = (int) *c;
    }
    lengths[lengths_size++] = 17;
    lengths[lengths_size++] = 31;
    lengths[lengths_size++] = 73;
    lengths[lengths_size++] = 47;
    lengths[lengths_size++] = 23;

    for (int i = 0; i != 64; i++) {
        run_round(circle, lengths, lengths_size, &current_position, &skip_size);
    }

    for (int i = 0; i != 16; i++) {
        xor = 0;
        for (int j = 0; j != 16; j++) {
            xor ^= circle[16*i + j];
        }
        sprintf(output + 2*i, "%02x", xor);
    }

    return output;
}

int main(int argc, char** argv)
{
    printf("%s\n", run(argv[1]));
    return 0;
}
