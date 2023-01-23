#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;
    int num[10];

    for (i = 0; i < 10; i++) {
        printf("input a number : ");
        scanf("%d", &num[i]);
    }
    
    for (i = 0; i < 10; i++)
        printf("num[%d] = %d\n", i, num[i]);
    
    
    return 0;
}
