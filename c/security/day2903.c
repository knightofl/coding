#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 2;
    printf("%d\n", a);
    
    _asm
    {
        add a, 0x05
        add a, 0x0a
    }

    printf("%d\n", a);
    
    return 0;
}
