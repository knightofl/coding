#include <stdio.h>


unsigned long long fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n-1);
}

int main(void) {
    int d = 20;	
    printf("%d! = %llu\n", d, fac(20));

    return 0;
}
