#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 10;

    _asm
    {
        pushad //eax, ecx, edx, ebx, esp, ebp, esi, edi 순서
        popad  //pushad 반대순서 
    }

    printf("%d\n", a);
    
    return 0;
}
