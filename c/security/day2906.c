#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;
    int c = 0;
	int d = 0;
    
    printf("%d %d %d %d\n", a, b, c, d);
    
    _asm
    {
	push eax

        mov a, 0x10
        mov b, 0x05
        inc b
            
        //xor eax, eax            
        add eax, a
        add eax, b
	mov c, eax

        //xor eax, eax
        mov eax, a
        sub eax, b 
	mov d, eax
            
	pop eax
    }

    printf("%d %d %d %d\n", a, b, c, d);
    
    return 0;
}
