#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int *pint = (int*) malloc(10);
    char *pch = (char*) malloc(20);

    int i;

    pint[0] = 10;
    pint[1] = 20;
    pint[2] = 30; // error!

    printf("sum : %d\n", pint[0] + pint[1] + pint[2]);

    for (i = 0; i < 10; i++)
        *(pch + i) = 0x61 + i;

    *(pch + i) = '\0';
    printf("%s\n", pch);

    free(pch);
    free(pint);
    
    return 0;
}
