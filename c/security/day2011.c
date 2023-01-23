#include <stdio.h>
#include <string.h>
#define MaxContent 1024

int crtxt(char *);

int inpname(char *);
int inpcont(char *);


int main(int argc, char *argv[])
{
    
    char name[256] = "c:\\";

    inpname(name);
    if(crtxt(name))
        printf("파일 쓰기에 성공했습니다.\n");

    return 0;
}

int crtxt(char *name)
{
    char content[MaxContent] = {0};
    FILE *fstream;
     
    fstream = fopen(name, "w");
    if (fstream) {
        printf("%s 파일이 생성되었습니다.\n", name);

        inpcont(content);
        fwrite(content, sizeof(char), sizeof(content), fstream);

        fclose(fstream);
        return 1;
    } else {
        printf("%s 파일을 생성할 수 없습니다.", name);
        return 0;
    }
}

int inpname(char *name)
{
    printf("파일 이름을 입력하세요.\n");
    scanf("%s", name+3);

    while (getchar() != '\n'); // 키버퍼 클리어
    return 0;
}

int inpcont(char *content)
{
    int i;
    char c;

    printf("파일 내용을 입력하세요.\n");

    for (i = 0; i < MaxContent; i++)
        if ((c = getchar()) != EOF)
            content[i] = c;
        else {
            content[i] = '\0';
            break;
        }

    return 0;
}
