#include <stdio.h>

int main(int argc, char *argv[])
{
    char c;

    printf("type a letter : ");
    scanf("%c", &c);

    switch (c = (c>='a' && c<='z') * 'a' + (c>='A' && c<='Z') * 'A') {
    case 'a':
	printf("small letter!\n");
	break;
    case 'A':
	printf("capital letter!\n");
	break;
    default:
	printf("not a letter!\n");
        break;	
    }
    
    return 0;
}
