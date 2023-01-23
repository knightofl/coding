#include <stdio.h>


int main(int argc, char *argv[]) {
    int a[5] = {0, 2, 4, 6, 8};
    int b[3][5] = {{0, 2, 4, 6, 8},
                   {10, 12, 14, 16, 18},
                   {20, 22, 24, 26, 28}};

    char c[3][6] ={"hello\0", "world\0", "happy\0"};

    int *p1 = a;
    int (*p2)[5] = b;
    char (*p3)[6] = c;
    char *p4[3] = {p3[0], p3[1], p3[2]};

    printf("%lu\n", sizeof(int));
    printf("%lu\n", sizeof(p1));
    printf("%lu\n", sizeof(p2));

    printf("%d\n", a[1]);
    printf("%d\n", *(a + 1));

    printf("%d\n", p1[1]);
    printf("%d\n", *(p1 + 1));

    printf("%p\n", p2);
    printf("%p\n", p2[0]);
    printf("%p\n", p2[1]);

    printf("%lu\n", p2[1] - p2[0]);

    printf("%u\n", p2[1][3]);
    printf("%d\n", *(p2[0] + 3));
    printf("%d\n", *(p2[1] + 3));

    printf("%d\n", (*++p2)[0]);

    printf("%s\n", c[0]);
    printf("%s\n", c[1]);

    printf("%s\n", *++p3);
    printf("%c\n", (*++p3)[1]);

    printf("%s\n", p4[0]);
    printf("%s\n", p4[1]);
    printf("%c\n", *++p4[0]);

    return 0;
}