#include <stdio.h>

int main(int argc, char *argv[])
{
    int num1, num2;
    
    scanf("%d %d", &num1, &num2);
    printf("%d\n", (num1<num2) ? num1 : num2);
    
    return 0;
}
