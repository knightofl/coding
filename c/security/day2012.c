#include <stdio.h>

float bmi_cal(float, float);
void bmi_q1(float bmi);
void bmi_q2(float bmi);

int main(int argc, char *argv[])
{
    float height, weight, bmi;
    char ch;

start:
    do {
        printf("======== BMI 지수 계산기 ========\n");
        printf("키(cm) 와 몸무게(kg) 을 입력하세요.\n");

        scanf("%f %f", &height, &weight);
    } while (height < 100 || height > 200 || weight < 30 || weight > 300);

    bmi = bmi_cal(height/100.0, weight);

    printf("============ 결과 ============\n");
    printf("당신의 BMI 지수는 %.2f 입니다.\n", bmi);
    bmi_q1(bmi);

    puts("");
    
    do {
        while(getchar() != '\n');
        printf("다시 하시겠습니까? (y/n) ");
        scanf("%c", &ch);
    } while (ch != 'y' && ch != 'n');

    if (ch == 'y') {
        system("cls");
        goto start;
    }
    
    return 0;
}

float bmi_cal(float height, float weight)
{
    return weight / (height * height);
}

void bmi_q1(float bmi)
{
    if (bmi < 18.5)
        printf("저체중입니다.\n");
    else if (bmi < 22.99)
        printf("정상체중입니다.\n");
    else {
        printf("과체중입니다. 운동을 시작하세요.\n");
        bmi_q2(bmi);
    }
}

void bmi_q2(float bmi)
{
    if (bmi < 24.99)
        printf("위험체중입니다.\n");
    else if (bmi < 29.99)
        printf("비만 1단계입니다.\n");
    else if (bmi < 39.99)
        printf("비만 2단계입니다.\n");
    else
        printf("비만 3단계입니다.\n");
}
