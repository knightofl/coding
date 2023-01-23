#include <stdio.h>

int main(int argc, char *argv[])
{
    int a = 1;

    while (a) {
	if (a > 110) {
	    printf("break\n");
	    break;
	}

	if (a > 100) {
	    a++;
	    printf("continue\n");
	    continue;
	}
	printf("a : %d\n", a++);
    }
    
    return 0;
}
