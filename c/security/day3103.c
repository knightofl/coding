#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;

    _asm
    {
        mov a, 0x0a
        mov b, 0x05

        mov eax, a
        add eax, b
        push eax
            
        mov eax, a
        sub eax, b
        push eax
            
        pop d
        pop c    
    }

    printf("%d %d %d %d\n", a, b, c, d);
    
    return 0;
}
