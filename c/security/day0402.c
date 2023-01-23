#include <stdio.h>

int main(int argc, char *argv[])
{
    char ch1 = 'b';
    char string[10];
    char ch2 = 'e';

    printf("Please enter the string : ");
    gets(string);

    printf("Character : %c\n", ch1);
    printf("Input string : %s\n", string);
    printf("Character : %c\n", ch2);
    
    return 0;
}
