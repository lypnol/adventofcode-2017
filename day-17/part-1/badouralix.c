#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
    int value;
    struct node_t* next;
} node_t;

node_t* node_create(int, node_t*);
node_t* node_insert(int, node_t*, unsigned int);
int node_value(node_t*, unsigned int);

int run(char* s)
{
	const int step_size = atoi(s),
              max_iter = 2017;
    unsigned int current_position = 0;
    node_t *buffer = node_create(0, NULL);

    for (int i = 1; i <= max_iter; i++) {
        current_position += step_size + 1;
        current_position %= i;
        buffer = node_insert(i, buffer, current_position);
    }

    return node_value(buffer, ++current_position);
}

int main(int argc, char** argv)
{
    if(argc < 2){
        printf("Missing one argument\n");
        exit(1);
    }
    printf("%d\n", run(argv[1]));
    return 0;
}

node_t* node_create(int value, node_t* next)
{
    node_t *node = (node_t*) malloc(sizeof(node_t));

    if (node == NULL) {
        printf("An error occured while trying to create a node\n");
        exit(0);
    }

    node->value = value;
    node->next = next;

    return node;
}

node_t* node_insert(int value, node_t* buffer, unsigned int position)
{
    if (position == 0) {
        return node_create(value, buffer);
    } else {
        if (buffer == NULL) {
            printf("An error occured while trying to insert a node: position greater than linked list length\n");
            exit(0);
        }
        return node_create(buffer->value, node_insert(value, buffer->next, --position));
    }
}

int node_value(node_t* node, unsigned int position)
{
    if (position == 0) {
        if (node == NULL) {
            printf("An error occured while trying to get node value: null node\n");
            exit(0);
        }
        return node->value;
    } else {
        if (node == NULL) {
            printf("An error occured while trying to get node value: position greater than linked list length\n");
            exit(0);
        }
        return node_value(node->next, --position);
    }
}
