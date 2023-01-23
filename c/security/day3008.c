#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 1;

    printf("%d\n", a);

    _asm
    {
        push a
        push 0x10    
        push eax
        pop eax
        pop a
        pop ebx    
    }

    printf("%d\n", a);
    
    return 0;
}
