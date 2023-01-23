#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 10;
    printf("%d\n", a);

    _asm
    {
        and a, 0x06
    }

    printf("%d\n", a);
    
    return 0;
}
