#include <stdio.h>
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int f19(int, int);

int main(int argc, char *argv[])
{
    int x, y;
    int sum;

    printf("input 2 numbers : ");
    scanf("%d %d", &x, &y);
    
    sum = f19(x, y);

    printf("even sum : %d\n", sum);
    
    return 0;
}

int f19(int x, int y)

{
    int i;
    int sum = 0;
    
    for (i = min(x, y); i <= max(x,y); i++)
        if (i%2 == 0)
            sum += i;
        else
            printf("%d\n", i);

    return sum;
}
