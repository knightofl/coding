#include <stdio.h>

int main(int argc, char *argv[])
{
    int value1 = 0;
    float value2 = 0;
    char ch = 0;

    printf("value1에 1000을 입력받으세요.\n");
    scanf("%d", &value1);
    while (getchar() != '\n');//fflush(stdin);
    
    printf("value2에 99.9를 입력받으세요.\n");
    scanf("%f", &value2);
    while (getchar() != '\n');//fflush(stdin);
    
    printf("ch에 \'X\'를 입력받으세요.\n");
    scanf("%c", &ch);
    while (getchar() != '\n');//fflush(stdin);

    printf("value1=10, value2=5.5, ch=\'X\'를 입력받고 출력하세요.\n");
    scanf("%d %f %c", &value1, &value2, &ch);

    printf("value1=%d, value2=%.1f, ch=%c", value1, value2, ch);
    
    
    return 0;
}
