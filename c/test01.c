#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *a, *b;
    int c, d;

    c = sizeof(int);
    printf("%d\n", c);

    a = malloc(c);
    b = malloc(c);

    *a = 1;
    *b = 1;

    c = (*a)++;
    d = ++*b;

    printf("%d %d %d %d\n", *a, *b, c, d);

    return 0;
}
