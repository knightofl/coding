#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("%d\n", -4 + 6 * 5 + 3);
    printf("%d\n", 3 - 7 % 8 + 5);
    printf("%d\n", -5 * 3 % 2 / 4);
    printf("%d\n", (8 + 7) % 6 / 2);

    printf("%d\n", 15 % -4);
    printf("%d\n", -15 % 4);
    printf("%d\n", -15 < -4);
    
    return 0;
}
