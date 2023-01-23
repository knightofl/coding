#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 2;
    printf("%d\n", a);
    
    _asm
    {
        sub a, 0x03
    }

    printf("%d\n", a);
    
    return 0;
}
