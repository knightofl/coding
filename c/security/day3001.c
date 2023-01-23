#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 0;
    int b = 0;
    int c = 0;
    
    printf("%d %d %d\n", a, b, c);
    
    _asm
    {
	push eax
        
        mov a, 0x03
        mov b, 0x05
	mov c, 0x0a

        inc b
	dec c
            
        mov eax, b
        add eax, c
	mov a, eax

        //mov eax, a
        sub eax, c 
	mov b, eax
            
	pop eax
    }

    printf("%d %d %d\n", a, b, c);
    
    return 0;
}
