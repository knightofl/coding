#include <stdio.h>

int main(int argc, char *argv[])
{
    typedef struct mydata
    {
        int a;
        int b;
        char c;
    } mydata;

    mydata data1;
    mydata *pdata;

    pdata = &data1;

    data1.a = 5;
    pdata->b = 10;
    pdata->c = 'a';

    printf("%d\n", pdata->a);
    printf("%d\n", data1.b);
    printf("%c\n", data1.c);
    
    return 0;
}
