#include <stdio.h>

int global = 30;

int main(int argc, char *argv[])
{
    int addr = 0;
    int value = 0;

    _asm
    {
        mov eax, offset global
        mov addr, eax

        mov ebx, [eax]
        mov value, ebx    
    }

    printf("addr : %p\n", addr);
    printf("value : %d\n", value);
    
    return 0;
}
