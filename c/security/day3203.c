#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char *str1 = "Hello, World!!";
    char str2[20];
    int len = strlen(str1);

    _asm
    {
        mov esi, dword ptr [str1]
        lea edi, dword ptr [str2]
        mov ecx, len
        rep movs byte ptr [edi], byte ptr [esi]
        mov byte ptr [edi], 0x00
    }

    printf("%s\n", str2);
    
    return 0;
}
