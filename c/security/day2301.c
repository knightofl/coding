#include <stdio.h>

int main(int argc, char *argv[])
{
    char a[5] = "Test";
    char *b = "Test";

    printf("%s\n", a);
    printf("%s\n", b);

    a[0] = 'Z';
    b[0] = 'Z';

    printf("%s\n", a);
    printf("%s\n", b);
    
    return 0;
}
