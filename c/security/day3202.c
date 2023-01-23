#include <stdio.h>

int main(int argc, char *argv[])
{
    char buffer[20];

    _asm
    {
        mov eax, 0x00
        lea edi, dword ptr [buffer]
        mov ecx, 0x05    
        rep stos dword ptr [edi]
    }

    printf("%s\n", buffer);
    
    return 0;
}
