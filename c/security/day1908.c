#include <stdio.h>

int main(int argc, char *argv[])
{
    int num;
    
    printf("input a number : ");
    scanf("%d", &num);

    if (check(num))
        printf("1 부터 100 사이의 수입니다.\n");
    else
        printf("1 부터 100 사이의 수가 아닙니다.\n");

    return 0;
}

int check(int num)
{
    return (num >=1 && num <= 100);
}
