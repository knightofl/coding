#include <stdio.h>

int __fastcall cdecl_test(int a, int b, int c)
{
    int sum = 0;
    sum = a + b + c;

    return 0;
}

int main(int argc, char *argv[])
{
    cdecl_test(1, 2, 3);
    
    return 0;
}
