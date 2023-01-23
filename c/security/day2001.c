#include <stdio.h>

void swap(int, int);

int main(int argc, char *argv[])
{
    int x = 10, y = 20;

    printf("1. x= %d, y = %d\n", x, y);

    swap(x, y);

    printf("4. x= %d, y = %d\n", x, y);
    
    return 0;
}

void swap(int x, int y)
{
    int temp;

    printf("2. x= %d, y = %d\n", x, y);

    temp = x;
    x = y;
    y = temp;

    printf("3. x= %d, y = %d\n", x, y);
}
