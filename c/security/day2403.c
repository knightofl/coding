#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int *pInt1, *pInt2;
    int size = 3;
    
    pInt1 = (int*) malloc(sizeof(int) * size);
    pInt2 = (int*) calloc(sizeof(int), size);

    while (size--) {
        printf("pint1[%d] : %d\n", size, pInt1[size]);
        printf("pint2[%d] : %d\n", size, pInt2[size]);
    }

    printf("\n");

    size = 5;
    pInt1 = (int*) realloc(pInt1, sizeof(int) * size);
    pInt2 = (int*) realloc(pInt2, sizeof(int) * size);

    while (size--) {
        printf("pint1[%d] : %d\n", size, pInt1[size]);
        printf("pint2[%d] : %d\n", size, pInt2[size]);
    }

    free(pInt1);
    free(pInt2);

    pInt1 = pInt2 = NULL;

    return 0;
}
