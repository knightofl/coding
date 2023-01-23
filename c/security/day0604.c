#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 1;
    int b = 0;
    int c = -1;

    printf("%d\n", a || b);
    printf("%d\n", b || c);
    printf("%d\n", a && b);
    printf("%d\n", a && c);
    printf("%d\n", b && c);
    printf("%d\n", !a);
    printf("%d\n", !b);
    
    return 0;
}
