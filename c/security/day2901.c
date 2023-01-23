#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    printf("%d\n", a);
    
    _asm
	{
		inc a
		inc a
	}

    printf("%d\n", a);
    
    return 0;
}
