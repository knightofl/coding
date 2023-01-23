#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 5;

    _asm
    {
        jmp L1
        mov a, 0x01

        L1:
        mov a, 0x02
    }

    printf("%d\n", a);
    
    return 0;
}
