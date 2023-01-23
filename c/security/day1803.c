#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fout;
    int i, j;

    fout = fopen("c:\\i2sec99.ii", "w");
    
    for (i = 2; i < 100; i++)
        for (j = 1; j < 10; j++)
            fprintf(fout, "%d*%d=%d\n", i, j, i*j);
    
    return 0;
}
