#include <stdio.h>

void hello(char *str)
{
    printf("Hello %s!!\n", str);
}


int main(int argc, char *argv[])
{
    void (* funcPointer)(char *);

    funcPointer = hello;
    funcPointer("World");
    
    return 0;
}
