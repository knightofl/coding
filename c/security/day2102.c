#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 10;
    int *pa, **ppa, ***pppa;

    pa = &a;
    ppa = &pa;
    pppa = &ppa;

    printf("%d\n", ***pppa);
    
    return 0;
}
