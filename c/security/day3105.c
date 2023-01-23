#include <stdio.h>

int main(int argc, char *argv[])
{
    int value = 1;
    printf("%x\n", value);

    _asm
    {
        mov word ptr value, 0x11111111
    }

    printf("%x\n", value);

    _asm
    {
        mov dword ptr value, 0x11111111
    }

    printf("%x\n", value);

    _asm
    {
        mov word ptr value, 0x12345678
    }

    printf("%x\n", value);

    _asm
    {
        mov byte ptr value, 0x33445566
    }

    printf("%x\n", value);
    
    
    return 0;
}
