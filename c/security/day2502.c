#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char* string = "Hello, World!";
    int len;

    len = strlen(string);

    printf("string = %s\n", string);
    printf("len = %d\n", len);
    
    return 0;
}
