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


    printf("국어 : ");
    scanf("%d", &stu1.kor);

    printf("수학 : ");
    scanf("%d", &stu1.math);

    printf("영어 : ");
    scanf("%d", &stu1.eng);

    printf("컴퓨터 : ");
    scanf("%d", &stu1.com);

    sco = stu1.kor + stu1.math + stu1.eng + stu1.com;
    avg = sco / 4;

    printf("총점 : %d, 평균 : %d\n", sco, avg);    
    
    return 0;
}
