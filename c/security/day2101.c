#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 1;
    int b = 2;
    char c = 'z';

    int *pa;
    int *pb;
    char *pc;

    pa = &a;
    pb = &b;
    pc = &c;

    printf("pa : 0x%08x\n", pa);
    printf("pb : 0x%08x\n", pb);
    printf("pc : 0x%08x\n", pc);

    printf("\n");

    printf("pa : %d \n", *pa);    
    printf("pb : %d \n", *pb);
    printf("pc : %c \n", *pc);
    
    return 0;
}
