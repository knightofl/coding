#include <stdio.h>

int __cdecl cdecl_test(int a, int b)
{
    int sum = 0;
    sum = a + b;

    return 0;
}

int main(int argc, char *argv[])
{
    cdecl_test(1, 2);
    
    return 0;
}
