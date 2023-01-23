#include <stdio.h>
int mul(int, int, int);

int main(int argc, char *argv[])
{
    int result, num1, num2, num3;
    result = num1 = num2 = num3;

    printf("Input three numbers : ");
    scanf("%d %d %d", &num1, &num2, &num3);

    result = mul(num1, num2, num3);
    printf("result : %d\n", result);
        
    return 0;
}

int mul(int a, int b, int c)
{
    return a * b * c;
}
