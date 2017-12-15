#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FACTOR_A 16807
#define FACTOR_B 48271
#define LIMIT 40000000

const int run(char* s)
{
    long a, b = atoi(strrchr(s, ' ') + 1);
    int result = 0;
    const char newline[] = "\n",
               *token = strtok(s, newline);
    token = '\0';
    a = atoi(strrchr(s, ' ') + 1);

    for (int i = 0; i < LIMIT; i++) {
        a = (a * FACTOR_A) % 0x7fffffff;
        b = (b * FACTOR_B) % 0x7fffffff;

        result += ((a ^ b) & 0xffff) == 0;
    }

    return result;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
