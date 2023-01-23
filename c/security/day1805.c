#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fin, *fout;
    char buf = 0;
    int i = 3;
    
    fin = fopen("c:\\test.txt", "r");
    fout = fopen("c:\\copy.txt", "w");

    while (i--) {
        if (fin)
            buf = fgetc(fin);
        else
            printf("can't read c:\\test.txt\n");

        if (fout)
            fputc(buf, fout);
        else
            printf("can't write c:\\copy.txt\n");
    }
     
    return 0;
}
