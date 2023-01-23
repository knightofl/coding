#include <stdio.h>

int main(int argc, char *argv[])
{
    int a;

    printf("input a number : ");
    scanf("%d", &a);

    if (a % 4 == 0)
	printf("a 는 4의 배수.\n");
    else
	printf("a 는 의 배수가 아님.\n");
    
    return 0;
}
