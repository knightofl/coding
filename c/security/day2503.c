#include <stdio.h>

int slen(char *);

int main(int argc, char *argv[])
{
    char* string = "Hello, World!";
    int len;

    len = slen(string);

    printf("string = %s\n", string);
    printf("len = %d\n", len);
    
    return 0;
}

int slen(char* str)
{
    int len = 0;
    while (str[len++]);
    
    return len - 1;
}
