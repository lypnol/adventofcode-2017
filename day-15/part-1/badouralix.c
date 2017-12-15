#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define FACTOR_A 0x41a7
#define FACTOR_B 0xbc8f
#define LIMIT 40000000

const int run(char* s)
{
    int64_t a, b = atoi(strrchr(s, ' ') + 1),
            result = 0;
    const char *token = strtok(s, "\n");
    token = '\0';
    a = atoi(strrchr(s, ' ') + 1);

    for (int i = 0; i < LIMIT; i++) {
        a = ((a * FACTOR_A) & 0x7fffffff) + ((a * FACTOR_A) >> 31);
        a -= (a > 0x7fffffff) * 0x7fffffff;

        b = ((b * FACTOR_B) & 0x7fffffff) + ((b * FACTOR_B) >> 31);
        b -= (b > 0x7fffffff) * 0x7fffffff;

        result += ((a ^ b) & 0xffff) == 0x0000;
    }

    return result;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
