#include <stdio.h>

typedef struct Su
{
    int odd;
    int even;
} NUM;

NUM Func(int a, int b)
{
    NUM s2;
    int tmp;

    s2.even = 0;
    s2.odd = 0;

    if (a > b)
    {
        tmp = a;
        a = b;
        b = tmp;
    }
	
    for(; a < b ; a++)
    {
        if(a%2 == 0)
            s2.even += a;
        else
            s2.odd += a;
    }

    return s2;
}
	
int main()
{
    NUM s1;
	
    s1 = Func(0, 10);

    printf("even = %d, odd = %d\n", s1.even, s1.odd);
	
    return 0;
}
