#include <stdio.h>

int main(int argc, char *argv[])
{
    int a;

    printf("input a number : ");
    scanf("%d", &a);

    if (a % 4 == 0)
	printf("a �� 4�� ���.\n");
    else
	printf("a �� �� ����� �ƴ�.\n");
    
    return 0;
}
