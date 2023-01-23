#include <stdio.h>

int main(int argc, char *argv[])
{
    int num[] = {0, 1, 2, 3, 4};
    int *pNum;

    int i;
    
    pNum = num;

    for (i = 0; i < 5; i++)
        printf("num[%d] = %d\n", i, num[i]);
    printf("\n");

    for (i = 0; i < 5; i++)
        printf("pNum[%d] = %d\n", i, pNum[i]);
    printf("\n");

    for (i = 0; i < 5; i++)
        printf("*(num + %d) = %d\n", i, *(num+i));
    printf("\n");

    for (i = 0; i < 5; i++)
        printf("*(pNum + %d) = %d\n", i, *(pNum+i));
    
    return 0;
}
