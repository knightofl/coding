#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 2;
    printf("%d\n", a);
    
    _asm
    {
        dec a
        dec a
    }

    printf("%d\n", a);
    
    return 0;
}
