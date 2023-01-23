#include <stdio.h>

int main(int argc, char *argv[])
{
    int num = 0;
    float f = 0;

    printf("input a number : ");
    scanf("%f", &f);

    num = (int)(f * 100) % 100;
    
    printf("number : %d", num);
    
    return 0;
}
