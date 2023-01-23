#include <stdio.h>

int main(int argc, char *argv[])
{
    int gugu = 9;
    int num;
    printf("input number : ");
    scanf("%d", &num);

    while(gugu > 0) {
        printf("%d * %d = %d\n", num, gugu, num*gugu);
        gugu--;
    }

    return 0;
}
