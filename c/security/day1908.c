#include <stdio.h>

int main(int argc, char *argv[])
{
    int num;
    
    printf("input a number : ");
    scanf("%d", &num);

    if (check(num))
        printf("1 ���� 100 ������ ���Դϴ�.\n");
    else
        printf("1 ���� 100 ������ ���� �ƴմϴ�.\n");

    return 0;
}

int check(int num)
{
    return (num >=1 && num <= 100);
}
