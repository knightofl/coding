#include <stdio.h>

int main(int argc, char *argv[])
{
    char c;   

    do {
        printf("Please type a capital letter : ");
        scanf("%c", &c);
	
	while (getchar() != '\n'); // cleaning key buffer
    } while (c < 'A' || c > 'Z');

    printf("Your small letter is \'%c\'.\n", c - 'A' + 'a');
    
    return 0;
}
