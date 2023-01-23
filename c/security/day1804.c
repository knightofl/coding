#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fout;
    int i, j, k;

    fout = fopen("c:\\dic.txt", "w");
    
    for (i = 'a'; i <= 'z'; i++)
        for (j = 'a'; j <= 'z'; j++)
            for (k = 'a'; k <= 'z'; k++)
                fprintf(fout, "%c%c%c\n", i, j, k);
    
    return 0;
}
