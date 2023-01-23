#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fin, *fout;
    char buf[100] = {0};
    
    fin = fopen("c:\\test.txt", "r");
    fout = fopen("c:\\copy.txt", "w");

    if (fin)
        fscanf(fin, "%s", buf);
    else
        printf("can't read c:\\test.txt\n");

    if (fout)
        fprintf(fout, "%s", buf);
    else
        printf("can't write c:\\copy.txt\n");

    return 0;
}
