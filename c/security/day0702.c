#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 10;
    float b = 3.14;
    double c = 99.9;

    printf("a + b = %d\n", a + b);
    printf("b + c = %c\n", b + c);

    printf("a + b = %d\n", a + (int)b);
    printf("b + c = %c\n", (char)(b + c));
    printf("(char)b + (char)c = %c\n", (char)b + (char)c);

    printf("a + b = %d\n", a + b);
    printf("b + c = %c\n", b + c);
    
    return 0;
}
