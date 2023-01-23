#include <stdio.h>

int sum()
{
    int a = 1;
    int b = 2;

    printf("func result : %d\n", a+b);

    return a+b;
}

int main(int argc, char *argv[])
{
    int result = 0;

    _asm
    {
        call sum
        mov result, eax    
    }

    printf("main result : %d\n", result);

    return 0;
}
