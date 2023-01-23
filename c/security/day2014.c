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

    printf("입력");
    inpname(file_o_name);
    handling_message();

    if ((file_o = fopen(file_o_name, "r")))
        printf("%s 파일을 읽는데 성공했습니다.\n", file_o_name);
    else {
        printf("%s 파일을 읽는데 실패했습니다.\n", file_o_name);
        return -1;
    }

    printf("복제");
    inpname(file_c_name);
    handling_message();

    if ((file_c = fopen(file_c_name, "w")))
        printf("%s 파일생성에 성공했습니다.\n", file_c_name);
    else {
        printf("%s 파일생성에 실패했습니다.\n", file_c_name);
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

    printf("파일 카피에 성공했습니다.\n");
    
    return 0;
}

int inpname(char *name)
{
    printf("파일의 이름을 입력하세요.\n");
    scanf("%s", name);

    while (getchar() != '\n'); // 키버퍼 클리어
    return 0;
}

int handling_message(void)
{
    int i, j;
    
    printf("파일처리중 ");

    for (i = 0; i < 5; i++) {
        printf("*");
        for (j = 200000000; j > 0; j--);
    }

    printf("\n");
    
    return 0;
}
