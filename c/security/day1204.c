#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int coin;
    int guess;
    
    srand(time(NULL));
    
    do {
        coin = rand() % 2 + 1;
	
	printf("===== ���� �յ� ���߱� ���� =====\n");
        printf("���ڸ� �Է��� �ּ��� (1.�ո� / 2. �޸�) : ");
	
	scanf("%d", &guess);

	if (coin == guess)
	    printf("�¾ҽ��ϴ�.\n\n");
	else
	    printf("Ʋ�Ƚ��ϴ�.\n\n");
    } while (guess == 1 || guess == 2);

    printf("1�� 2 �̿��� ���ڸ� �Է��ϼ̳׿�. �ȳ��� ������.\n");
    
    return 0;
}
