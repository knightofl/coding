#include <stdio.h>

int main(int argc, char *argv[])
{
    int num = 0;

    while (num < 100)
	printf("%d\t", ++num);

    printf("\n");

    while (num > 0)
	printf("%d\t", num--);
       
    return 0;
}
