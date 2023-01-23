#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 4;

    printf("%d\n", a);

    _asm
    {
        shl a, 0x01
    }

    printf("%d\n", a);

    _asm
    {
        shr a, 0x02
    }

    printf("%d\n", a);
    
    return 0;
}
