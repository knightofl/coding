#include <stdio.h>
#include <string.h>

void upsideDown(char *, int);

int main(int argc, char *argv[])
{
    char s[4096];
    
    do {
    printf("�ܾ �Է��ϼ���.\n");

    gets(s);
    upsideDown(s, strlen(s));
    
    } while(strcmp(s, "END"));

    printf("END �� �ԷµǸ� ���α׷��� �����մϴ�.\n");
          
    return 0;
}

void upsideDown(char *s, int size)
{
    int i;

    for (i = size - 1; i >= 0; i--)
            printf("%c", s[i]);

    printf("\n");
}
