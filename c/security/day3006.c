#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;

    printf("%d\n", a);

    _asm
    {
        mov eax, 0x12345678
        mov a, eax    
    }

    printf("%d\n", a);

    _asm
    {
        xor eax, eax
        mov a, eax   
    }

    printf("%d\n", a);
    
    return 0;
}
