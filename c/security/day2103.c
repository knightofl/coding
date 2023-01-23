#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int isRepeat(int []);
void pitch(int []);
void bat(int []);
void judge(int *, int *, int *, int *);

int main(int argc, char *argv[])
{
    int pitchBall[3];
    int batBall[3];
    int round;
    int ball, strike;
    char replay;

    do {
        system("cls");
        
        printf("*************************************************\n");
        printf("****                �� �� �� ��              ****\n");
        printf("*************************************************\n\n");

        pitch(pitchBall);
        round = 1;
    
        do {
            printf("%dȸ�Դϴ�. ", round);
            bat(batBall);
            judge(pitchBall, batBall, &strike, &ball);

            printf("%d ��Ʈ����ũ, %d ���Դϴ�.\n\n", strike, ball);
        } while (round++ < 9 && strike != 3);

        if (strike == 3) {
            printf("������ϴ�. ");
            if (round <= 3)
                printf("����Ʈ ����!\n");
            else if (round <= 6)
                printf("�ݵ����!\n");
        } else {
            printf("���� %d%d%d, ", pitchBall[0], pitchBall[1], pitchBall[2]);
            printf("������ ���߽��ϴ�.\n");
        }

        do {
            printf("�� ������ �Ͻðڽ��ϱ�? (y/n) : ");
            replay = getchar();
            while (getchar() != '\n');
        } while (replay != 'y' && replay != 'n');
    
    } while (replay == 'y');
    
    return 0;
}


int isRepeat(int *num)
{
    int i, j;

    for (i = 0; i < 2; i++)
        for (j = i+1; j < 3; j++)
            if (num[i] == num[j])
                return 1;

    return 0;
}

void pitch(int *ball)
{
    srand(time(NULL));

    do {
        ball[0] = rand() % 9 + 1;
        ball[1] = rand() % 9 + 1;
        ball[2] = rand() % 9 + 1;
    } while (isRepeat(ball));
}

void bat(int *ball)
{
    int num;
    
Loop:
    printf("1���� 9���� �ߺ� ���� ���� 3���� �Է��ϼ���. : ");
    scanf("%d", &num);

    if (getchar() != '\n') {
        while (getchar() != '\n');
        goto Loop;
    }

    if (num < 111 || num > 999)
        goto Loop;
       
    ball[0] = num / 100;
    num %= 100;
    ball[1] = num / 10;
    ball[2] = num % 10;

    if (ball[0] == 0 || ball[1] == 0 || ball[2] == 0)
        goto Loop;

    if (isRepeat(ball))
        goto Loop;
}

void judge(int *pitchBall, int *batBall, int *strike, int *ball)
{
    int i, j;
    *strike = 0;
    *ball = 0;
    
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            if (pitchBall[i] == batBall[j])
                if (i == j)
                    (*strike)++;
                else
                    (*ball)++;
}
