#include <stdio.h>
#include <stdlib.h>

int x;      // uninitialized data
int y = 15; // initialized data

int main(int argc, char *argv[])
{
    int *values;
    int i;

    values = (int *)malloc(sizeof(int) * 5);

    for (i = 0; i < 5; i++)
        values[i] = i;

    return 0;
}