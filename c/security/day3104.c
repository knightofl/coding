#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 10;

    _asm
    {
        pushad //eax, ecx, edx, ebx, esp, ebp, esi, edi ����
        popad  //pushad �ݴ���� 
    }

    printf("%d\n", a);
    
    return 0;
}
