#include <stdio.h>
char efun(int, char);

int main(int argc, char *argv[])
{
    int a;
    a = efun(4, 'k');
    printf("\n%d\n", a);
    
    return 0;
}


char efun(int a, char b)
{
    putchar(b);
    return a;
}
