#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int com;
    int player;
    
    srand(time(NULL));
    
    int count = 6;
    com = rand() % 101 + 1;

    puts("=====  ���� ���߱� ���� =====");
    printf("��ȸ�� ��� %d��.\n", count);

    while (count) {
	do {
	    printf("1���� 100 ������ ���ڸ� �Է��� �ּ��� : ");
	    scanf("%d", &player);
	    while(getchar() != '\n'); // ���� Ŭ����
        } while (player<0 || player>100);
 
	if (com > player)
	    printf("���� ��ȸ %dȸ. �׺��� �����ϴ�.\n", --count);
	else if (com < player)
	    printf("���� ��ȸ %dȸ. �׺��� �����ϴ�.\n", --count);
	else if (com == player) {
	    printf("�¾ҽ��ϴ�.\n");
	    break;
	}
    }

    if (!count)
	printf("Ʋ�Ƚ��ϴ�.\n");
    
    return 0;
}

