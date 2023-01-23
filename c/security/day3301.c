#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 3;

    _asm
    {
        test a, 0x02
    }

    printf("%d\n", a);
    
    return 0;
}
