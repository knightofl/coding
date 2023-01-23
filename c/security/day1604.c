#include <stdio.h> 
#define min(a, b) (((a) < (b)) ? (a) : (b))


int main()
{
    int i = 0;
    int j = 0;
    int tmp;

    printf("input i, j : ");
    scanf("%d %d", &i, &j);

    if (min(i, j) == j) {
        tmp = i;
        i = j;
        j = tmp;
    }

    while (i <= j)
    {
        printf("%d\n", i);
        i++; 
    }

    return 0;
}
