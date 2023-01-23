#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 5;

    _asm
    {
        cmp a, 0x05
    }

    printf("%d\n", a);
    
    return 0;
}
