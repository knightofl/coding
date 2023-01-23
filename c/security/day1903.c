#include <stdio.h>

char toupper(char);

int main(int argc, char *argv[])
{
    char ch;
    
    printf("Input a small letter : ");
    ch = getchar();
    printf("to upper : %c", toupper(ch));
        
    return 0;
}

char toupper(char a)
{
    return a - 'a' + 'A';
}
