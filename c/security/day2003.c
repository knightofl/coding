#include <stdio.h>

int calc(int, int, char);
int inp(int *, int *, char *);

int main(int argc, char *argv[])
{
    int num1, int num2;
    char cal;

    inp(&num1, &num2, char cal);    
    calc();
    
    return 0;
}

int calc(int num1, int num2, char cal)
{
    switch (cal) {
    case '+': 
        printf("%d + %d = %d", num1, num2, num1 + num2);
    case '-': 
        printf("%d - %d = %d", num1, num2, num1 - num2);    
    case '*': 
        printf("%d * %d = %d", num1, num2, num1 * num2);
    case '/': 
        printf("%d / %d = %d", num1, num2, num1 / num2);
    }

    return 0;    
}

int inp(int *num1, int *num2, char *cal)
{
    char s[200];

    int i;
    *num1 = 0;
    *num2 = 0;


    printf("수식을 입력하세요. : ");
    scanf("%s", s);

    for (i = 0; i < 200; i++)
        


}

