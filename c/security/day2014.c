#include <stdio.h>
#include <string.h>

int inpname(char *);
int handling_message();
int cptxt(FILE *, FILE *);

int main(int argc, char *argv[])
{
    char file_o_name[256] = {'\0'};
    char file_c_name[256] = {'\0'};

    FILE *file_o, *file_c;

    printf("�Է�");
    inpname(file_o_name);
    handling_message();

    if ((file_o = fopen(file_o_name, "r")))
        printf("%s ������ �дµ� �����߽��ϴ�.\n", file_o_name);
    else {
        printf("%s ������ �дµ� �����߽��ϴ�.\n", file_o_name);
        return -1;
    }

    printf("����");
    inpname(file_c_name);
    handling_message();

    if ((file_c = fopen(file_c_name, "w")))
        printf("%s ���ϻ����� �����߽��ϴ�.\n", file_c_name);
    else {
        printf("%s ���ϻ����� �����߽��ϴ�.\n", file_c_name);
        return -1;
    }

    handling_message();
    cptxt(file_o, file_c);

    fclose(file_c);
    fclose(file_o);


    return 0;
}

int cptxt(FILE *file_o, FILE *file_c)
{
    char content = '\0';

    while ((content = fgetc(file_o)) != EOF)
        fputc(content, file_c);

    printf("���� ī�ǿ� �����߽��ϴ�.\n");
    
    return 0;
}

int inpname(char *name)
{
    printf("������ �̸��� �Է��ϼ���.\n");
    scanf("%s", name);

    while (getchar() != '\n'); // Ű���� Ŭ����
    return 0;
}

int handling_message(void)
{
    int i, j;
    
    printf("����ó���� ");

    for (i = 0; i < 5; i++) {
        printf("*");
        for (j = 200000000; j > 0; j--);
    }

    printf("\n");
    
    return 0;
}
