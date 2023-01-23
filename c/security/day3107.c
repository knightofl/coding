#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 4;

    printf("%.8x\n", a);
    printf("%.8x\n", &a);

    _asm
    {
        mov eax, [ebp-0x04]
        mov a, eax
    }

    printf("%.8x\n", a);   

    _asm
    {
        lea eax, [ebp-0x04]
        mov a, eax
    }

    printf("%.8x\n", a);   

    
    return 0;
}
