#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 97;
    int* b = &a;

    printf("10진수 : %d\n", a);
    printf("08진수 : %o\n", a);
    printf("16진수 : %x\n", a);
    printf("문자 : %c\n", 'a');
    printf("문자 : %c\n", a);
    printf("문자 hex : %c\n", 0x61);
    printf("문자 oct : %c\n", 0141);
    printf("문자 dec : %c\n", 97);
    printf("문자열 : %s\n", "string");
    printf("주소 : %p\n", &a);
    printf("b : %p\n", b);
    printf("*b = %d\n", *b);
    printf("*&a : %d\n", *&a);

    return 0;
}
