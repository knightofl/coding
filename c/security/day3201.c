#include <stdio.h>

int main(int argc, char *argv[])
{
    char buffer[20];

    _asm
    {
        mov eax, 0x00
        lea edi, dword ptr [buffer]
        stos dword ptr [edi]
    }

    printf("%s\n", buffer);
    
    return 0;
}
