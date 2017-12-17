#include <stdio.h>
#include <stdlib.h>

const int run(char* s)
{
	const int step_size = atoi(s),
              max_iter = 50*1000*1000;
    int current_position = 0,
        result = 0;

    for (int i = 1; i <= max_iter; i++) {
        current_position += step_size;

        if (current_position >= i) {
            if (i < step_size) {
                current_position %= i;
            } else {
                current_position -= i;
            }
        }

        if (current_position == 0) {
            result = i;
        }

        current_position++;
    }

    return result;
}

int main(int argc, char** argv)
{
    printf("%d\n", run(argv[1]));
    return 0;
}
