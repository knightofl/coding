#include <stdio.h>
#include <string.h>

void upsideDown(char *, int);

int main(int argc, char *argv[])
{
    char s[4096];
    
    do {
    printf("단어를 입력하세요.\n");

    gets(s);
    upsideDown(s, strlen(s));
    
    } while(strcmp(s, "END"));

    printf("END 가 입력되면 프로그램을 종료합니다.\n");
          
    return 0;
}

void upsideDown(char *s, int size)
{
    int i;

    for (i = size - 1; i >= 0; i--)
            printf("%c", s[i]);

    printf("\n");
}
