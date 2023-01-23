#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    srand(time());

    printf("rand() = %d\n", rand());
    printf("rand() = %d\n", rand());
    printf("rand() = %d\n", rand());
    
    return 0;
}
