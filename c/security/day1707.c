#include <stdio.h>
#include <string.h>


int main(void)
{
    int i;
    char s[20] = "Hello, World!"; // 13 + NULL

    printf("strlen(s) = %d\n", strlen(s));
    printf("sizeof(s) = %d\n", sizeof(s));
    
    for (i = 0; i < 20; i++)
	printf("%d  ", s[i]);


    return 0;
}
