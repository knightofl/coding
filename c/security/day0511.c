#include <stdio.h>

int main(int argc, char *argv[])
{
    int num[5];
    int i;

    for (i = 0; i < 5; i++) {
        printf("Input number%d : ", i+1);
        scanf("%d", &num[i]);
    }
    
    printf("%d + %d + %d + %d + %d = %d", num[0], num[1], num[2], num[3],
	   num[4], num[0] + num[1] + num[2] + num[3] + num[4]);
    
    return 0;
}
