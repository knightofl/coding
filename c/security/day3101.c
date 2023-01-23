#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;

    _asm
    {
        push eax
        mov eax, 0x03

        push eax
        pop a

        push 0x05
        pop b

        pop eax
    }

    printf("%d %d\n", a, b);
    
    return 0;
}
