#include <stdio.h>

int main(void)    
{
    typedef struct score
    {
        int kor;
        int math;
        int eng;
        int com;
    } score;

    score stu1;

    int sco, avg;


    printf("���� : ");
    scanf("%d", &stu1.kor);

    printf("���� : ");
    scanf("%d", &stu1.math);

    printf("���� : ");
    scanf("%d", &stu1.eng);

    printf("��ǻ�� : ");
    scanf("%d", &stu1.com);

    sco = stu1.kor + stu1.math + stu1.eng + stu1.com;
    avg = sco / 4;

    printf("���� : %d, ��� : %d\n", sco, avg);    
    
    return 0;
}
