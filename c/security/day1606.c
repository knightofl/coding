#include <stdio.h>

int main(int argc, char *argv[])
{
    char ch;

    do {
        scanf("%c", &ch);
        printf("%x\n", ch);
        while (getchar() != '\n');
    }while (ch != 'x');
    
    return 0;
}
