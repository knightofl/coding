#include <stdio.h>

int main(int argc, char *argv[])
{
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    _asm
    {
        mov eax, a
        cmp eax, b
        jb S1
        mov eax, b    
        S1:
        cmp eax, c    
        jb S2
        mov eax, c
        S2:
        mov a, eax    
    }

    printf("%d\n", a);

    return 0;
}
