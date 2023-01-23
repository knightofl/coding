#include <stdio.h>

int main(void)
{
    int num;
    int i;

    printf("input number : ");
    scanf("%d", &num);

    for (i = 1; i < 101; i++) {
        if (i%3 == 0) {
            printf("%d\t", i);
            if (!--num)
                break;
        }
    }

    return 0;
}
