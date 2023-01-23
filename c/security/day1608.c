#include <stdio.h>

int main(int argc, char *argv[])
{
    int gugu = 1;
    int num;
    printf("input number : ");
    scanf("%d", &num);

    while(gugu < 10) {
        printf("%d * %d = %d\n", num, gugu, num*gugu);
        gugu++;
    }

    return 0;
}
