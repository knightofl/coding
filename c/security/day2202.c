#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int i;
    int num[10];

    srand(time(NULL));

    for (i = 0; i < 10; i++)
        num[i] = rand();
    
    
    for (i = 0; i < 10; i++)
        printf("num[%d] = %d\n", i, num[i]);
    
    
    return 0;
}
