#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char src[20] = "Hello World!";
    char dst[20] = {'\0'};
    char *tmp;

    printf("dst : %s\n", dst);

    tmp = strcpy(dst, src);
    
    printf("tmp : %s\n", tmp);
    printf("dst : %s\n", dst);
    printf("src : %s\n", src);

    printf("tmp address : %p\n", tmp);
    printf("dst address : %p\n", dst);
    printf("src address : %p\n", src);
    
    return 0;
}
