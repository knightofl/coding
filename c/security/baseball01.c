#include <stdio.h>
#define MAX 10000


int main(void)
{
    int nan[MAX];
    int i, j;

    for (i = 0; i < MAX; i++)
	nan[i] = 0;
    
    for (i = 0; i < 32768; i++) {
	j = i % MAX;
	nan[j]++;
    }

    for (i = 0; i < MAX; i++)
	printf("[%d] = %d\t", i, nan[i]);

    return 0;
}
