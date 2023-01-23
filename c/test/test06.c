#include <stdio.h>

int and(int x1, int x2) {
    return x1 && x2;
}


int main(void) {

    printf("%d", and(1, 2));
    return 0;
}
