#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 9;
    printf("%d\n", a);

    _asm
    {
        or a, 0x07
    }

    printf("%d\n", a);
    
    return 0;
}
