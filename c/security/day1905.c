#include <stdio.h>
int fun(char *);

int main(int argc, char *argv[])
{
    char s[100];

    printf("Input a string : ");
    scanf("%s", s);

    fun(s);
        
    return 0;
}

int fun(char *a)
{
    printf("%s\n", a);
    return 0;
}
