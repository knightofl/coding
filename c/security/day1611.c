#include <stdio.h>

int main()
{
    int i, j, k;
    int sum = 0;

    printf("input 2 numbers : ");
    scanf("%d %d", &i, &j);

    for (k = i; k <= j; k++)
        if (k%5 != 0) {
            sum += k;
            printf("%d\t", k);
        }
    printf("\nsum : %d\n", sum);

    return 0;
}
