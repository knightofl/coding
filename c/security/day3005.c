#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 12;

    printf("%d\n", a);

    _asm
    {
        xor a, 0x08
    }

    printf("%d\n", a);

    _asm
    {
        xor a, 0x08
    }

    printf("%d\n", a);
    
    return 0;
}
