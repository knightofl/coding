#include <stdio.h>

int main(int argc, char *argv[])
{
    int num[5];
    int i;

    for (i = 0; i < 5; i++) {
        printf("Input number%d : ", i+1);
        scanf("%d", &num[i]);
    }

    for (i = 0; i < 5; i++) {
        printf("Number%d : %d\n", i+1, num[i]+10);
    }
    
    return 0;
}
