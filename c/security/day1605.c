#include <stdio.h>
#define min(a, b) (((a) < (b)) ? (a) : (b))

int main(int argc, char *argv[])
{
    int a, b, c;
    
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n", min(min(a, b), c));    
    
    return 0;
}
