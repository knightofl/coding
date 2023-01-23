#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 3;
    int b = 1;
    int c = 6;
    int d = 3;

    printf("(a - b) * (c - d) / (a + d) = %d\n", (a - b) * (c - d) / (a + d));
    
    return 0;
}
