#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char string[20] = "apapple";
    char *search = "app";
    char *result;

    result = strstr(string, search);

    printf("string address : %p\n", string);
    printf("result address : %p\n", result);
    printf("result : %s\n", result);
    
    return 0;
}
