#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 97;
    int* b = &a;

    printf("10���� : %d\n", a);
    printf("08���� : %o\n", a);
    printf("16���� : %x\n", a);
    printf("���� : %c\n", 'a');
    printf("���� : %c\n", a);
    printf("���� hex : %c\n", 0x61);
    printf("���� oct : %c\n", 0141);
    printf("���� dec : %c\n", 97);
    printf("���ڿ� : %s\n", "string");
    printf("�ּ� : %p\n", &a);
    printf("b : %p\n", b);
    printf("*b = %d\n", *b);
    printf("*&a : %d\n", *&a);

    return 0;
}
