#include <stdio.h>
int fun(char *);

int main(int argc, char *argv[])
{
    fun("Hello I2sec");
        
    return 0;
}

int fun(char *a)
{
    int i = 0;
    while (a[i++] != ' ');
    while (putchar(a[i++]));

    return 0;
}
