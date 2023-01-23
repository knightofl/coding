#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fout;
    int i;

    fout = fopen("c:\\dic.txt", "w");
    
    for (i = 0; i < 10000; i++)
        fprintf(fout, "i2sec%04d\n", i);
    
    return 0;
}
