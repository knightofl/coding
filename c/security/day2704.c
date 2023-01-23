#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char p[5000] ={0};
    int i[] = {35,174,174,231,37,135,135,157,157,157,25,223,\
              162,241,162,223,106,162,105,25,96,143,107,135,\
              157,6,223,54,6,107,162,135,157,143,157,25,231,35,231};
    int j;

    FILE *doc = fopen("c:\\level8.txt", "r");

    if (doc)
        fread(p, 5000, 1, doc);

    for (j = 0; j < 39; j++)
        putchar(p[i[j]]);

    return 0;
}
