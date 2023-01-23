#include <stdio.h>

int main(int argc, char *argv[])
{
    int num1;
    int num2;
    
    printf("Input a number : ");
    scanf("%d", &num1);
    
    printf("Input a number : ");
    scanf("%d", &num2);

    printf("%d - %d = %d\n", num1, num2, num1 - num2);
    printf("%d * %d = %d\n", num1, num2, num1 * num2);
    
    return 0;
}
