#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int inpNum(void); // 1���� 100������ ���� �Է¹޾� ��ȯ.
int match(int, int); // �̱�� 1, ���� 0 ��ȯ.

int main(int argc, char *argv[])
{
    int com;
    int count = 6;
    char game;

    srand(time(NULL));

    do {
	com = rand() % 101 + 1;

	puts("=====  ���� ���߱� ���� =====");
	printf("��ȸ�� ��� %d���Դϴ�.\n", count);

	if (match(com, count))
	    printf("������ϴ�!! ");
	else
	    printf("������ ���߽��ϴ�. ");

	printf("�ٽ� �Ͻðڽ��ϱ�? (y/n) : ");
	scanf("%c", &game);
    } while (game == 'y');
    
    return 0;
}



int match(int com, int count)
{
    int player;

    while (count) {
	player = inpNum();

	if (com == player)
	    return 1;
	else if (com > player)
	    printf("�׺��� �����ϴ�. ���� ��ȸ�� %dȸ.\n", --count);
	else
	    printf("�׺��� �����ϴ�. ���� ��ȸ�� %dȸ.\n", --count);
    }

    return 0;
}


int inpNum(void)
{
    int num;
    
    do {
	printf("1���� 100 ������ ���ڸ� �Է��� �ּ��� : ");
	scanf("%d", &num);
	while(getchar() != '\n'); // ���� Ŭ����
    } while (num<1 || num>100);
	
    return num;
}
