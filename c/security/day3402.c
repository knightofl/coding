#include <stdio.h>

int main(int argc, char *argv[])
{
    int a, b, c;

    scanf("%d %d", &a, &b);

    _asm
    {
        mov eax, a
        cmp eax, b
        mov c, eax
        jnb GOOD
        mov eax, b
        mov c, eax
    }

GOOD:
    printf("%d\n", c);

    return 0;
}
