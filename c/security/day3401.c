#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 5;

    _asm
    {
        LABEL:
        inc a
        cmp a, 0x05
        jne LABEL
    }        

    printf("%d\n", a);
    
    return 0;
}
