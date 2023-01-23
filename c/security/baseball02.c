#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 1000
#define TIMES 1000

int main(void)
{
    int nan[MAX];
    int i, j;
    srand(time(NULL));
    
    for (i = 0; i < MAX; i++)
	nan[i] = 0;
    
    for (i = 0; i < MAX * TIMES; i++) {
	j = rand() % MAX;
	nan[j]++;
    }

    for (i = 0; i < MAX; i++)
	printf("[%d] = %d\t", i, nan[i]);

    return 0;
}
