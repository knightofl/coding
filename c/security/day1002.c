#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    for (i = 3; i < 77; i++)
	printf("%d\t", i);

    printf("\n");
    
    for (i = 87; i > 11; i--)
	printf("%d\t", i);

    
    return 0;
}
