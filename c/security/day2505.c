#include <stdio.h>

char* scpy(char *, char *);

int main(int argc, char *argv[])
{
    char src[20] = "Hello World!";
    char dst[20] = {'\0'};
    char *tmp;

    printf("dst : %s\n", dst);

    tmp = scpy(dst, src);
    
    printf("tmp : %s\n", tmp);
    printf("dst : %s\n", dst);
    printf("src : %s\n", src);

    printf("tmp address : %p\n", tmp);
    printf("dst address : %p\n", dst);
    printf("src address : %p\n", src);
    
    return 0;
}

char* scpy(char* dst, char* src)
{
    int i = 0;

    do {
        dst[i] = src[i];
    } while (src[i++]);

    return dst;
}
