#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("size of int = %d\n", sizeof(int));
    printf("size of short = %d\n", sizeof(short));
    printf("size of char = %d\n", sizeof(char));
    printf("size of long = %d\n", sizeof(long));
    printf("size of long long = %d\n", sizeof(long long));
    putchar('\n');

    printf("size of float = %d\n", sizeof(float));
    printf("size of double = %d\n", sizeof(double));
    printf("size of long double = %d\n", sizeof(long double));
    
    return 0;
}
