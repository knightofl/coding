#include <stdio.h>

void evenOdd(int *, int);

int main(int argc, char *argv[])
{
    int size;
    int num[10];

    size = sizeof(num) / sizeof(int);
    evenOdd(num, size);
        
    return 0;
}

void evenOdd(int *num, int size)
{
    int i = size;
    int even = 0;
    int odd = 0;

    for (i = 0; i < size; i++) {
        printf("input a number : ");
        scanf("%d", &num[i]);

        if (num[i]%2 == 0)
            even++;
        else odd++;
    }

    printf("even number : %d\n", even);
    printf("odd number : %d\n", odd);
}
