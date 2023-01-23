#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    printf("%d\n", a);
    
    _asm
    {
        mov a, 0x05
    }

    printf("%d\n", a);
    
    return 0;
}
