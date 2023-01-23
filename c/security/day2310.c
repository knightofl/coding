#include <stdio.h>
#include <string.h>

void upsideDown(char *, int);

int main(int argc, char *argv[])
{
    char s[4096];
    
    printf("문장을 입력하세요.\n");

    gets(s);
    upsideDown(s, strlen(s));
    
    return 0;
}

void upsideDown(char *s, int size)
{
    int i = 0;

    for (i = 0; i < size; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            printf("%c", s[i] - 'a' + 'A');
        else if (s[i] >= 'A' && s[i] <= 'Z')
            printf("%c", s[i] - 'A' + 'a');
        else
            printf("%c", s[i]);
}
