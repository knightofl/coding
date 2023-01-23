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
        printf("���� ���⿡ �����߽��ϴ�.\n");

    return 0;
}

int crtxt(char *name)
{
    char content[MaxContent] = {0};
    FILE *fstream;
     
    fstream = fopen(name, "w");
    if (fstream) {
        printf("%s ������ �����Ǿ����ϴ�.\n", name);

        inpcont(content);
        fwrite(content, sizeof(char), sizeof(content), fstream);

        fclose(fstream);
        return 1;
    } else {
        printf("%s ������ ������ �� �����ϴ�.", name);
        return 0;
    }
}

int inpname(char *name)
{
    printf("���� �̸��� �Է��ϼ���.\n");
    scanf("%s", name+3);

    while (getchar() != '\n'); // Ű���� Ŭ����
    return 0;
}

int inpcont(char *content)
{
    int i;
    char c;

    printf("���� ������ �Է��ϼ���.\n");

    for (i = 0; i < MaxContent; i++)
        if ((c = getchar()) != EOF)
            content[i] = c;
        else {
            content[i] = '\0';
            break;
        }

    return 0;
}
