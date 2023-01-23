#include <stdio.h>

void crypt(char *);

int main(int argc, char *argv[])
{
    char a[] = "My name is JSM";
    char *p;
    p = a;

    printf("source : %s\n", p);

    crypt(p);
    printf("incode : %s\n", p);
    
    return 0;
}

void crypt(char *source)
{
    while(*source)
        *source++ += 1;
}
