#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;
    int c = 0;

    _asm
    {
        push 0x0a
        push 0x14
        push 0x1e    

        pop ecx
        pop ebx
        pop eax    

        mov a, eax
        mov b, ebx
        mov c, ecx
    }

    printf("%d %d %d\n", a, b, c);
    
    return 0;
}
