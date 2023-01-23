#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;
    int c = 0;
    int sum = 0;

    _asm
    {
        push eax
            
        mov a, 0x0a
        mov b, 0x14
        mov c, 0x1e

        mov eax, a
        add eax, b
        sub eax, c    

        mov sum, eax

        pop eax    
     }

    printf("%d\n", sum);
    
    return 0;
}
