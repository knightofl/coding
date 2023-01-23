#include <stdio.h>

int main(int argc, char *argv[])
{
    int sum, even, odd;
    int num;

    sum = even = odd = 0;

    while (1) {
        printf("input number : ");
        scanf("%d", &num);

        if (num == -1)
	    break;
	
        if (num%2 == 0)
            even++;
        else if (num%2 == 1)
            odd++;

        sum += num;
    }

    printf("even: %d, odd: %d, sum:%d\n", even, odd, sum);

    return 0;
}
