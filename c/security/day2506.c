#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char dst[20] = "Hello";
    char cat[20] = " World!";
    char *tmp;

    printf("dst: %s\n", dst);

    tmp = strcat(dst, cat);

    printf("tmp : %s\n", tmp);
    printf("dst : %s\n", dst);
    
    printf("tmp address : %p\n", tmp);
    printf("dst address : %p\n", dst);
    
    return 0;
}
