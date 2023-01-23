#include <stdio.h>

void incArr(int *, int);

int main(int argc, char *argv[])
{
    int size;
    int num[5] = {10, 20, 30, 40, 50};
    int i;

    size = sizeof(num) / sizeof(int);
    incArr(num, size);
        
    for (i = 0; i < size; i++)
        printf("%d\t", num[i]);
    
    return 0;
}

void incArr(int *num, int size)
{
    int i = size;

    for (i = 0; i < size; i++)
        num[i]++;
}
