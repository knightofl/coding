#include <stdio.h>

void upsideDown(char *);

int main(int argc, char *argv[])
{
    char s[4096];
    printf("문장을 입력하세요.\n");

    gets(s);
    upsideDown(s);
    
    return 0;
}

void upsideDown(char *s)
{
    int i = 0;

    for (i = 0; i < 4096, s[i] != 0; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            printf("%c", s[i] - 'a' + 'A');
        else if (s[i] >= 'A' && s[i] <= 'Z')
            printf("%c", s[i] - 'A' + 'a');
        else
            printf("%c", s[i]);
}
