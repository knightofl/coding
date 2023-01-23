#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char str1[10] = "Hello";
    char str2[10] = "He2lo";
    char str3[10] = "Heplo";

    int result;

    result = strcmp(str1, str2);
    printf("result : %d\n", result);

    result = strcmp(str1, str3);
    printf("result : %d\n", result);

    str2[2] = 'l';
    result = strcmp(str1, str2);
    printf("result : %d\n", result);
    
    return 0;
}
