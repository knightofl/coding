#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main()
{
    srand(time(NULL));

    printf("========show me your brain!========\n");
    int num1 = rand() / 10000; 
    int num2 = rand() / 10000;
    int reply;
    int answer = num1 + num2;

    alarm(3);
    
    printf("%d + %d = ?\n", num1, num2);
    scanf("%d", &reply);
    
    if (reply == answer)
        printf("You Win!\n");
    else
        printf("You Lose!\n");

    return 0;
}
