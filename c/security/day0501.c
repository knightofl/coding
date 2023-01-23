#include <stdio.h>

int main(int argc, char *argv[])
{
    int num = 0;
    signed char ch = 0;

    printf("Input Number : ");
    scanf("%d", &num);

    while(getchar() != '\n');
	
    scanf("%c", &ch);

    printf("num = %d, ch = %c", num, ch);
    
    return 0;
}
