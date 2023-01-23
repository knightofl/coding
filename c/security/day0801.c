#include <stdio.h>

int main(int argc, char *argv[])
{
    int num1 = 0;
    int num2 = 0;

    num1 = sizeof(num2);
    num2 = sizeof(char);

    printf("num1 : %d\n", num1++);
    printf("num2 : %d\n", num2--);

    printf("num1 : %d\n", num1 *= num2);

    num2 = --num1 && num2;

    printf("num2 : %d\n", num2);
    printf("sizeof : %d\n", sizeof(num1) * 4);
    printf("True of False : %d\n", num1 > num2);
    printf("True or False : %d\n", num1 == !num2);
    printf("True or False : %d\n", num1 != num2 || num2);
    
    return 0;
}
