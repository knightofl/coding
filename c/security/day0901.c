#include <stdio.h>

int main(int argc, char *argv[])
{
    int a, b;
    a = b = 0;

    printf("input a number : ");
    scanf("%d", &a);

    printf("input a number : ");
    scanf("%d", &b);

    if (a < 10)
	printf("a < 10\n");

    if (b > 5)
        printf("b > 5\n");
    else
	printf("b <= 5\n");
    
    return 0;
}
