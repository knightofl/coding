#include <stdio.h>

char* scat(char *, char *);
int slen(char *);

int main(int argc, char *argv[])
{
    char dst[20] = "Hello";
    char cat[20] = " World!";
    char *tmp;

    printf("dst: %s\n", dst);

    tmp = scat(dst, cat);

    printf("tmp : %s\n", tmp);
    printf("dst : %s\n", dst);
    
    printf("tmp address : %p\n", tmp);
    printf("dst address : %p\n", dst);

    return 0;
}

char* scat(char *dst, char *cat)
{
    int i;

    int dstNum = slen(dst);
    int catNum = slen(cat);

    for (i = 0; i <= catNum; i++)
        dst[dstNum + i] = cat[i];

    return dst;   
}

int slen(char* str)
{
    int len = 0;
    while (str[len++]);
    
    return len - 1;
}
