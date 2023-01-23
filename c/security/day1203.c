#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int i = 10;
    srand(time(NULL));
    
    while (i--) {
        printf("rand() = %d\n", rand());
    }
    return 0;
}
