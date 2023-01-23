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
        printf("======== BMI ���� ���� ========\n");
        printf("Ű(cm) �� ������(kg) �� �Է��ϼ���.\n");

        scanf("%f %f", &height, &weight);
    } while (height < 100 || height > 200 || weight < 30 || weight > 300);

    bmi = bmi_cal(height/100.0, weight);

    printf("============ ��� ============\n");
    printf("����� BMI ������ %.2f �Դϴ�.\n", bmi);
    bmi_q1(bmi);

    puts("");
    
    do {
        while(getchar() != '\n');
        printf("�ٽ� �Ͻðڽ��ϱ�? (y/n) ");
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
        printf("��ü���Դϴ�.\n");
    else if (bmi < 22.99)
        printf("����ü���Դϴ�.\n");
    else {
        printf("��ü���Դϴ�. ��� �����ϼ���.\n");
        bmi_q2(bmi);
    }
}

void bmi_q2(float bmi)
{
    if (bmi < 24.99)
        printf("����ü���Դϴ�.\n");
    else if (bmi < 29.99)
        printf("�� 1�ܰ��Դϴ�.\n");
    else if (bmi < 39.99)
        printf("�� 2�ܰ��Դϴ�.\n");
    else
        printf("�� 3�ܰ��Դϴ�.\n");
}
