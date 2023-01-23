#include <stdio.h>

int main(int argc, char *argv[])
{
    int a[] = {0, 1, 2, 3, 4, 5, 6};
    int b[][3] = {0, 1, 2, 3, 4, 5, 6};

    int *ptra;
    int (*ptrb)[3];

    ptra = a;
    ptrb = b;

    printf("int size = %d\n", sizeof(int));
    printf("a size = %d\n", sizeof(a));
    printf("b size = %d\n", sizeof(b));

    printf("ptra = %p\n", ptra);
    printf("ptrb = %p\n", ptrb);

    printf("&ptra[1] = %p\n", &ptra[1]);
    printf("&ptrb[1] = %p\n", &ptrb[1]);

    printf("ptra + 1 = %p\n", ptra + 1);
    printf("ptrb + 1 = %p\n", ptrb + 1);
	
    printf("ptra[1] = %d\n", ptra[1]);
    printf("ptrb[1] = %p\n", ptrb[1]);

    printf("&ptrb[1][0] = %p\n", &ptrb[1][0]);
    printf("ptrb[1][0] = %d\n", ptrb[1][0]);

    printf("ptrb[1] + 1 = %p\n", ptrb[1] + 1);
    printf("&ptrb[1][1] = %p\n", &ptrb[1][1]);

    return 0;
}
