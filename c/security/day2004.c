#include <stdio.h>
#define max(a, b) ((a) > (b) ? (a) : (b))

int main(int argc, char *argv[])
{
    int x, y;
    printf("Input 2 numbers.\n");
    scanf("%d %d", &x, &y);

    printf("%d\n", max(x, y));
    
    return 0;
}
