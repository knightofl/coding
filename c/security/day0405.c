#include <stdio.h>

int main(int argc, char *argv[])
{
    int value1 = 0;
    float value2 = 0;
    char ch = 0;

    printf("value1�� 1000�� �Է¹�������.\n");
    scanf("%d", &value1);
    while (getchar() != '\n');//fflush(stdin);
    
    printf("value2�� 99.9�� �Է¹�������.\n");
    scanf("%f", &value2);
    while (getchar() != '\n');//fflush(stdin);
    
    printf("ch�� \'X\'�� �Է¹�������.\n");
    scanf("%c", &ch);
    while (getchar() != '\n');//fflush(stdin);

    printf("value1=10, value2=5.5, ch=\'X\'�� �Է¹ް� ����ϼ���.\n");
    scanf("%d %f %c", &value1, &value2, &ch);

    printf("value1=%d, value2=%.1f, ch=%c", value1, value2, ch);
    
    
    return 0;
}
