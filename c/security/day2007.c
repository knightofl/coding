#include <stdio.h>

void gugu(int);

int main(int argc, char *argv[])
{
    int num;

    printf("input a number : ");
    scanf("%d", &num);

    gugu(num);
    
    return 0;
}

void gugu(int num)
{
    int i;
    for (i = 9; i > 0; i--)
        printf("%d * %d = %d\n", num, i, num * i);
}
