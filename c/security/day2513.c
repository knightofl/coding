#include <stdio.h>

char* schr(char *, char);

int main(int argc, char *argv[])
{
    char string[20] = "Hello, World!";
    char search = 'l';
    char *result;

    result = schr(string, search);

    printf("string address : %p\n", string);
    printf("result address : %p\n", result);
    printf("result : %s\n", result);
    
    return 0;
}

char* schr(char *str, char sch)
{
    int i = 0;
    
    do {
        if (str[i] == sch)
            return str + i;
    } while (str[i++]);

    return NULL;

}
